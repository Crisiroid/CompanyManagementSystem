### face_recognition.py
import cv2
import dlib
import numpy as np
from config import MODEL_PATHS
from db import store_face_model, get_face_model

# Load models
face_detector = cv2.dnn.readNetFromCaffe(MODEL_PATHS["prototxt"], MODEL_PATHS["caffemodel"])
landmark_predictor = dlib.shape_predictor(MODEL_PATHS["landmark"])
face_recognizer = dlib.face_recognition_model_v1("models/dlib_face_recognition_resnet_model_v1.dat")


def extract_face_features(image):
    blob = cv2.dnn.blobFromImage(image, scalefactor=1.0, size=(300, 300), mean=(104.0, 177.0, 123.0))
    face_detector.setInput(blob)
    detections = face_detector.forward()

    if detections.shape[2] == 0:
        return None

    box = detections[0, 0, 0, 3:7] * np.array([image.shape[1], image.shape[0], image.shape[1], image.shape[0]])
    (x1, y1, x2, y2) = box.astype("int")
    rect = dlib.rectangle(x1, y1, x2, y2)
    landmarks = landmark_predictor(image, rect)
    descriptor = face_recognizer.compute_face_descriptor(image, landmarks)
    return np.array(descriptor).tolist()


def compare_faces(face_model_1, face_model_2, threshold=0.6):
    distance = np.linalg.norm(np.array(face_model_1) - np.array(face_model_2))
    return distance < threshold