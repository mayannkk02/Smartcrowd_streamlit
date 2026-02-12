from ultralytics import YOLO
import torch

_loaded_models = {}

def load_model(model_choice):
    if model_choice not in _loaded_models:
        device = "cuda" if torch.cuda.is_available() else "cpu"
        model = YOLO(f"models/{model_choice}")
        model.to(device)
        _loaded_models[model_choice] = model
    return _loaded_models[model_choice]

def detect_people(frame, model_choice="yolov8n.pt"):
    model = load_model(model_choice)

    results = model(
        frame,
        conf=0.25,
        classes=[0],
        imgsz=480,
        verbose=False
    )

    detections = []

    for r in results:
        for box in r.boxes:
            x1, y1, x2, y2 = box.xyxy[0].tolist()
            conf = float(box.conf[0])

            detections.append({
                "bbox": [int(x1), int(y1), int(x2), int(y2)],
                "confidence": conf
            })

    return detections
