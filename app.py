from flask import Flask, render_template, send_from_directory
from azure.storage.blob import BlobServiceClient

app = Flask(__name__)

# Initialize the connection to Azure Blob Storage
connect_str = "mKeGwYHEkF9Ttc2YTOrK/aGQ+wysLk0aAwWZ17nqRb+vVd1nrdX6eHOcETgtq9Trrmgo6fOpA7gx+AStzseghg=="
blob_service_client = BlobServiceClient.from_connection_string(connect_str)
container_name = "images"

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/images/<category>')
def portfolio(category):
    # List all blobs in the container that match the category prefix
    container_client = blob_service_client.get_container_client(container_name)
    blob_urls = []
    for blob in container_client.list_blobs(name_starts_with=category):
        blob_url = f"https://{blob_service_client.account_name}.blob.core.windows.net/{container_name}/{blob.name}"
        blob_urls.append(blob_url)
    return render_template('portfolio.html', images=blob_urls, category=category)

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('.', path)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
