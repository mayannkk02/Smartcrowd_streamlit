import streamlit as st
import cv2

from ui.sidebar import sidebar_inputs
from smartcrowd_core.video_stream import get_video_capture
from smartcrowd_core.detection import detect_people
from smartcrowd_core.counting import count_people
from smartcrowd_core.alerts import generate_alert
from smartcrowd_core.utils import draw_detections, log_alert

# ------------------------------
# Streamlit Config
# ------------------------------
st.set_page_config(
    page_title="SmartCrowd",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🚦 SmartCrowd - Real-Time Crowd Monitoring")

# ------------------------------
# Sidebar Inputs
# ------------------------------
source_type, video_file, rtsp_url, scene_info, thresholds, model_choice = sidebar_inputs()

# ------------------------------
# Start Video Stream
# ------------------------------
if source_type:

    cap = get_video_capture(source_type, video_file, rtsp_url)

    if cap is None or not cap.isOpened():
        st.error("❌ Could not open video source.")
    else:
        stframe = st.empty()
        alert_placeholder = st.empty()

        frame_count = 0
        latest_detections = []

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # Resize for speed
            frame = cv2.resize(frame, (640, 480))

            frame_count += 1

            # Frame skipping for performance
            if frame_count % 2 == 0:
                latest_detections = detect_people(
                    frame,
                    model_choice=model_choice
                )

            # Counting
            count, density = count_people(latest_detections, frame.shape)

            # Alerts
            status, suggestion = generate_alert(
                count,
                density,
                thresholds,
                scene_info
            )

            # Draw detections
            frame = draw_detections(frame, latest_detections)

            # Display info
            alert_placeholder.markdown(
                f"""
                **👥 Count:** {count}  
                **📏 Density:** {density:.6f}  
                **🚨 Status:** {status}  
                **💡 Suggestion:** {suggestion}
                """
            )

            # Log
            log_alert(count, density, status, suggestion)

            # Convert BGR → RGB
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            stframe.image(frame_rgb, channels="RGB", use_container_width=True)

        cap.release()
        st.success("✅ Video processing finished.")
