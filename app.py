from flask import Flask, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'index.html')

@app.route('/about')
def about():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'about.html')

if __name__ == '__main__':
    app.run(debug=True)
