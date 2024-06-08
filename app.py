import os
from flask import Flask, render_template
from azure.storage.blob import BlobServiceClient

app = Flask(__name__)

# Get the connection string from environment variable
connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')

# Create the BlobServiceClient object
blob_service_client = BlobServiceClient.from_connection_string(connect_str)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/portfolio/<category>')
def portfolio(category):
    container_client = blob_service_client.get_container_client('images')
    blob_list = container_client.list_blobs(name_starts_with=category + '/')
    image_urls = [container_client.url + '/' + blob.name for blob in blob_list]
    return render_template('portfolio.html', images=image_urls, category=category)

if __name__ == "__main__":
    app.run(debug=True)
