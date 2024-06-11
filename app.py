from flask import Flask, request, jsonify
from azure.storage.blob import BlobServiceClient
import os

app = Flask(__name__)

# Azure Blob Storage connection string
connection_string = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
if not connection_string:
    raise ValueError("No Azure Storage connection string found in environment variables")

blob_service_client = BlobServiceClient.from_connection_string(connection_string)

@app.route('/')
def home():
    return "Welcome to the Azure Blob Storage Flask app!"

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part in the request", 400
    
    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400

    try:
        blob_client = blob_service_client.get_blob_client(container="mycontainer", blob=file.filename)
        blob_client.upload_blob(file)
        return f"File {file.filename} uploaded successfully.", 200
    except Exception as e:
        return str(e), 500

@app.route('/list', methods=['GET'])
def list_files():
    try:
        container_client = blob_service_client.get_container_client("mycontainer")
        blob_list = container_client.list_blobs()
        files = [blob.name for blob in blob_list]
        return jsonify(files)
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
