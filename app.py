from flask import Flask, request, jsonify
import os
from azure.storage.blob import BlobServiceClient

app = Flask(__name__)

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
    # Example: Fetch images from Azure Blob Storage for the given category
    container_client = blob_service_client.get_container_client('images')
    blob_list = container_client.list_blobs(name_starts_with=category)
    image_urls = [blob.url for blob in blob_list]
    return jsonify(image_urls)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
