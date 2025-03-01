### config.py
import os

DB_CONFIG = {
    "server": "localhost",
    "database": "ComapnyManagementDB",
    "driver": "ODBC Driver 17 for SQL Server",
    "trusted_connection": "yes"
}


MODEL_PATHS = {
    "prototxt": "models/deploy.prototxt",
    "caffemodel": "models/res10_300x300_ssd_iter_140000_fp16.caffemodel",
    "landmark": "models/shape_predictor_68_face_landmarks.dat"
}