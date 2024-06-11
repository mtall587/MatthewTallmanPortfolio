from flask import Flask, request, jsonify, send_from_directory
import os
from azure.storage.blob import BlobServiceClient

app = Flask(__name__, static_url_path='/static')

connection_string = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

@app.route('/')
def home():
    return '<h1>Welcome to My Portfolio</h1><a href="/portfolio">Go to Portfolio</a>'

@app.route('/portfolio')
def portfolio():
    return '<h1>Portfolio</h1><button onclick="loadImages(\'Damien\')">Damien</button><button onclick="loadImages(\'Jason\')">Jason</button><div id="image-gallery" class="image-gallery"></div><script src="/static/script.js"></script>'

@app.route('/get_images')
def get_images():
    category = request.args.get('category')
    container_client = blob_service_client.get_container_client(category)
    blob_list = container_client.list_blobs()
    images = [f"https://{blob_service_client.account_name}.blob.core.windows.net/{category}/{blob.name}" for blob in blob_list]
    return jsonify(images)

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
