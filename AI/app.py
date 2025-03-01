### app.py
from flask import Flask, request, jsonify
import cv2
import numpy as np
from face_recognition import extract_face_features, compare_faces
from db import store_face_model, get_face_model

app = Flask(__name__)

@app.route("/register", methods=["POST"])
def register():
    file = request.files["image"]
    user_id = request.form["user_id"]
    image = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)
    face_model = extract_face_features(image)
    if face_model:
        store_face_model(user_id, str(face_model))
        return jsonify({"status": "success", "message": "Face model stored successfully."})
    return jsonify({"status": "error", "message": "Face not detected."})

@app.route("/verify", methods=["POST"])
def verify():
    file = request.files["image"]
    user_id = request.form["user_id"]
    image = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)
    new_face_model = extract_face_features(image)
    if new_face_model:
        stored_face_model = get_face_model(user_id)
        if stored_face_model and compare_faces(eval(stored_face_model), new_face_model):
            return jsonify({"status": "success", "message": "Identity verified."})
        return jsonify({"status": "error", "message": "Identity mismatch."})
    return jsonify({"status": "error", "message": "Face not detected."})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)