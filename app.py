import os
from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='.')

@app.route('/')
def serve_index():
    # Serves the index.html from the root folder
    return send_from_directory('.', 'index.html')

if __name__ == '__main__':
    # Render configures the PORT dynamically via environment variables
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
