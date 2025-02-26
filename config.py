import os

# ==============================
# Database configuration for SQL Server
# ==============================
DB_CONFIG = {
    'SERVER': 'your_server_name',
    'DATABASE': 'your_database_name',
    'USERNAME': 'your_username',
    'PASSWORD': 'your_password',
    'DRIVER': '{ODBC Driver 17 for SQL Server}'
}

# ==============================
# Paths and file configurations
# ==============================
MODEL_DIR = "models/"
FACE_DATA_FILE = os.path.join(MODEL_DIR, "face_data.pickle")
SHAPE_PREDICTOR_FILE = os.path.join(MODEL_DIR, "shape_predictor_68_face_landmarks.dat")
DEPLOY_FILE = os.path.join(MODEL_DIR, "deploy.prototxt")

# ==============================
# Security settings
# ==============================
SECRET_KEY = 'your_secret_key'

# ==============================
# API service configurations
# ==============================
API_CONFIG = {
    'FACE_RECOGNITION_API_URL': 'http://localhost:5000/api/recognize',
    'REGISTER_USER_API_URL': 'http://localhost:5000/api/register'
}

# ==============================
# Server and port configurations
# ==============================
SERVER_CONFIG = {
    'HOST': '0.0.0.0',
    'PORT': 5000
}

# ==============================
# Logging settings
# ==============================
LOGGING_CONFIG = {
    'LOG_FILE': 'app.log',
    'LOG_LEVEL': 'DEBUG',
}

# ==============================
# Other settings
# ==============================
ALLOWED_IMAGE_EXTENSIONS = ['jpg', 'jpeg', 'png']
MAX_IMAGE_SIZE = 5 * 1024 * 1024
