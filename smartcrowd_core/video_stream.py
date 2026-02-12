import cv2
import tempfile

def get_video_capture(source_type, video_file=None, rtsp_url=None):
    """
    Returns a cv2.VideoCapture object based on user input.
    - source_type: "Upload File" or "Webcam/RTSP"
    - video_file: Streamlit UploadedFile (if upload)
    - rtsp_url: webcam index (0,1,2) or RTSP URL
    """
    if source_type == "Upload File" and video_file is not None:
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
        temp_file.write(video_file.read())
        temp_file.close()
        return cv2.VideoCapture(temp_file.name)

    elif source_type == "Webcam/RTSP" and rtsp_url is not None:
        try:
            source = int(rtsp_url)  # webcam index
        except ValueError:
            source = rtsp_url       # RTSP string
        return cv2.VideoCapture(source)

    return None
