from waitress import serve
from app import app  # Replace 'your_flask_app_file' with the actual file name where your Flask 'app' is defined

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8080)
