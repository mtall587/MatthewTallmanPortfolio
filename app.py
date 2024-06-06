from flask import Flask, send_from_directory

app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

# Route for the portfolio page
@app.route('/portfolio')
def portfolio():
    return send_from_directory('.', 'portfolio.html')

# Route for static files like CSS, JS, and images
@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('.', path)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
