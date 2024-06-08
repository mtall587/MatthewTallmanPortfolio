import os
from flask import Flask, render_template, jsonify
from azure.storage.blob import BlobServiceClient

app = Flask(__name__)

# Load connection string from environment variable
connection_string = os.getenv('AZURE_STORAGE_CONNECTION_STRING')

if not connection_string:
    raise ValueError("AZURE_STORAGE_CONNECTION_STRING environment variable not set")

# Initialize the BlobServiceClient
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# Define the categories and container names
categories = {
    'damien': 'Damien',
    'jason': 'Jason'
}

@app.route('/')
def portfolio():
    return render_template('portfolio.html')

@app.route('/category/<category>')
def get_images_by_category(category):
    if category not in categories:
        return jsonify({"error": "Category not found"}), 404

    container_name = 'images'
    folder_name = categories[category]
    container_client = blob_service_client.get_container_client(container_name)

    blob_list = container_client.list_blobs(name_starts_with=folder_name + '/')
    image_urls = [
        f"https://{blob_service_client.account_name}.blob.core.windows.net/{container_name}/{blob.name}"
        for blob in blob_list
    ]

    return jsonify(image_urls)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
