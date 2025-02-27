import pyodbc
import hashlib


SERVER = 'your_server_name'
DATABASE = 'your_database_name'
USERNAME = 'your_username'
PASSWORD = 'your_password'


def create_connection():
    try:
        conn = pyodbc.connect(
            f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}')
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None


def register_user_db(username, password, face_encoding):
    try:

        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        conn = create_connection()
        if conn is None:
            return False

        cursor = conn.cursor()

        cursor.execute("INSERT INTO Users (username, password, face_encoding) VALUES (?, ?, ?)",
                       (username, hashed_password, str(face_encoding)))
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Error in register_user_db: {e}")
        return False


def authenticate_user_db(username, password):
    try:

        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        conn = create_connection()
        if conn is None:
            return None

        cursor = conn.cursor()

        cursor.execute("SELECT face_encoding FROM Users WHERE username = ? AND password = ?",
                       (username, hashed_password))
        result = cursor.fetchone()

        conn.close()

        if result:

            return result[0]
        else:
            return None
    except Exception as e:
        print(f"Error in authenticate_user_db: {e}")
        return None


def get_all_users_db():
    try:

        conn = create_connection()
        if conn is None:
            return None

        cursor = conn.cursor()

        cursor.execute("SELECT username, face_encoding FROM Users")
        users = cursor.fetchall()

        conn.close()

        return users
    except Exception as e:
        print(f"Error in get_all_users_db: {e}")
        return None
