import face_recognition
import cv2
import numpy as np
import os
import pickle

MODEL_DIR = "models/"

FACE_DATA_FILE = os.path.join(MODEL_DIR, "face_data.pickle")


def register_user(image, name):
    try:

        img = face_recognition.load_image_file(image)

        face_encoding = face_recognition.face_encodings(img)

        if len(face_encoding) == 0:
            return False

        if os.path.exists(FACE_DATA_FILE):
            with open(FACE_DATA_FILE, "rb") as f:
                known_face_encodings, known_face_names = pickle.load(f)
        else:
            known_face_encodings = []
            known_face_names = []

        known_face_encodings.append(face_encoding[0])
        known_face_names.append(name)

        with open(FACE_DATA_FILE, "wb") as f:
            pickle.dump([known_face_encodings, known_face_names], f)

        return True

    except Exception as e:
        print(f"Error in register_user: {e}")
        return False


def authenticate_user(image):
    try:

        img = face_recognition.load_image_file(image)

        face_encoding = face_recognition.face_encodings(img)

        if len(face_encoding) == 0:
            return None

        if os.path.exists(FACE_DATA_FILE):
            with open(FACE_DATA_FILE, "rb") as f:
                known_face_encodings, known_face_names = pickle.load(f)
        else:
            return None

        matches = face_recognition.compare_faces(known_face_encodings, face_encoding[0])

        if True in matches:
            first_match_index = matches.index(True)
            return known_face_names[first_match_index]
        else:
            return None

    except Exception as e:
        print(f"Error in authenticate_user: {e}")
        return None


def extract_face_from_image(image_path):

    try:

        img = face_recognition.load_image_file(image_path)

        face_locations = face_recognition.face_locations(img)

        if len(face_locations) == 0:
            return None

        top, right, bottom, left = face_locations[0]
        face_image = img[top:bottom, left:right]

        return face_image

    except Exception as e:
        print(f"Error in extract_face_from_image: {e}")
        return None
