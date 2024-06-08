from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/images/<category>')
def show_images(category):
    images_path = os.path.join('static', 'images', category)
    if not os.path.exists(images_path):
        return "Category not found", 404

    images = [os.path.join(images_path, f'image{i}.jpg') for i in range(1, 26)]
    return render_template('portfolio.html', category=category, images=images)

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    app.run(debug=True)
