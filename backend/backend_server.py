import os
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # Enable CORS for frontend access

# Example: Read database URL from environment variable
db_url = os.environ.get('DATABASE_URL')

@app.route('/')
def index():
    return jsonify({
        "message": "OpenSCAD Backend is running!",
        "database_url_set": bool(db_url) # Check if DB URL is configured
    })

# Add your /render endpoint and other backend logic here...
# Remember to implement database connection and example fetching logic

if __name__ == '__main__':
    # Host 0.0.0.0 makes it accessible externally (within Docker network)
    # Port 5000 is exposed in Dockerfile and docker-compose
    app.run(host='0.0.0.0', port=5000, debug=True) # debug=True for development

