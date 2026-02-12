import numpy as np

def count_people(detections, frame_shape):
    """
    Count number of people and estimate density.
    - detections: list of bounding boxes
    - frame_shape: (height, width, channels)
    """
    count = len(detections)
    height, width, _ = frame_shape
    area = height * width
    density = count / area if area > 0 else 0
    return count, density
