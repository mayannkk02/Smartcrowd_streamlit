import cv2
import os
import csv
from datetime import datetime

def draw_detections(frame, detections):
    for det in detections:
        x1, y1, x2, y2 = det["bbox"]
        conf = det["confidence"]

        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        label = f"Person {conf:.2f}"
        cv2.putText(frame, label, (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (0, 255, 0), 2)

    return frame


def ensure_log_folder():
    folder_path = os.path.join("data", "logs")
    os.makedirs(folder_path, exist_ok=True)


def log_alert(count, density, status, suggestion):
    ensure_log_folder()

    file_path = os.path.join("data", "logs", "crowd_log.csv")

    file_exists = os.path.isfile(file_path)

    with open(file_path, mode="a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["Time", "Count", "Density", "Status", "Suggestion"])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            count,
            density,
            status,
            suggestion
        ])
