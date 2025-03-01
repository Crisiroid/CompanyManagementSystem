### config.py
import os

DB_CONFIG = {
    "server": "YOUR_SQL_SERVER",
    "database": "YOUR_DATABASE",
    "username": "YOUR_USERNAME",
    "password": "YOUR_PASSWORD",
    "driver": "ODBC Driver 17 for SQL Server"
}

MODEL_PATHS = {
    "prototxt": "models/deploy.prototxt",
    "caffemodel": "models/res10_300x300_ssd_iter_140000_fp16.caffemodel",
    "landmark": "models/shape_predictor_68_face_landmarks.dat"
}