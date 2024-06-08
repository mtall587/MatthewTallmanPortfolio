from flask import Flask, render_template, request, jsonify
from azure.storage.blob import BlobServiceClient
import os

app = Flask(__name__)

# Azure Blob Storage Configuration
AZURE_STORAGE_CONNECTION_STRING = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
CONTAINER_NAME = 'images'

blob_service_client = BlobServiceClient.from_connection_string(AZURE_STORAGE_CONNECTION_STRING)
container_client = blob_service_client.get_container_client(CONTAINER_NAME)

def list_blobs_in_category(category):
    blob_list = container_client.list_blobs(name_starts_with=f"{category}/")
    image_urls = []
    for blob in blob_list:
        image_url = f"https://{blob_service_client.account_name}.blob.core.windows.net/{CONTAINER_NAME}/{blob.name}"
        image_urls.append(image_url)
    return image_urls

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/get_images')
def get_images():
    category = request.args.get('category')
    if category in ['Damien', 'Jason']:
        images = list_blobs_in_category(category)
        return jsonify(images)
    else:
        return jsonify([])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
