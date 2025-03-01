### db.py
import pyodbc
from config import DB_CONFIG

def get_db_connection():
    conn_str = (
        f'DRIVER={{{DB_CONFIG["driver"]}}};'
        f'SERVER={DB_CONFIG["server"]};'
        f'DATABASE={DB_CONFIG["database"]};'
        f'UID={DB_CONFIG["username"]};'
        f'PWD={DB_CONFIG["password"]}'
    )
    return pyodbc.connect(conn_str)

def store_face_model(user_id, face_model):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE users SET face_model = ? WHERE id = ?", (face_model, user_id)
    )
    conn.commit()
    conn.close()

def get_face_model(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT face_model FROM users WHERE id = ?", (user_id,))
    row = cursor.fetchone()
    conn.close()
    return row[0] if row else None