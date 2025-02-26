from flask import Flask, request, jsonify
from face_recognition import register_user, authenticate_user
from db import register_user_db, authenticate_user_db

app = Flask(__name__)


@app.route('/authenticate', methods=['POST'])
def authenticate():
    try:
        image = request.files['image']

        user_name = authenticate_user(image)

        if user_name:
            return jsonify({"status": "success", "user": user_name}), 200
        else:
            return jsonify({"status": "failure", "message": "User not recognized"}), 401

    except Exception as e:
        return jsonify({"status": "failure", "message": str(e)}), 500


@app.route('/register', methods=['POST'])
def register():
    try:
        name = request.form['name']
        image = request.files['image']

        success = register_user(image, name)

        if success:
            return jsonify({"status": "success", "message": "User registered"}), 201
        else:
            return jsonify({"status": "failure", "message": "Face not detected"}), 400

    except Exception as e:
        return jsonify({"status": "failure", "message": str(e)}), 500


@app.route('/')
def home():
    return "Face Recognition API is running!", 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)
