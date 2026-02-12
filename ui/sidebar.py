import streamlit as st

def sidebar_inputs():
    st.sidebar.header("🎥 Video Source")
    source_type = st.sidebar.radio(
        "Select source",
        ["Upload File", "Webcam/RTSP"],
        index=0
    )

    video_file, rtsp_url = None, None

    if source_type == "Upload File":
        video_file = st.sidebar.file_uploader(
            "Upload a video",
            type=["mp4", "avi", "mov"]
        )
    else:
        rtsp_url = st.sidebar.text_input(
            "Enter webcam index (0,1,2) or RTSP link"
        )

    # ---------------- Scene Info ----------------
    st.sidebar.header("🏟 Scene Info")

    entries = st.sidebar.number_input("Number of Entries", min_value=0, value=1)
    exits = st.sidebar.number_input("Number of Exits", min_value=0, value=1)
    barricades = st.sidebar.checkbox("Barricades available?")
    guards = st.sidebar.checkbox("Guards available?")

    scene_info = {
        "entries": entries,
        "exits": exits,
        "barricades": barricades,
        "guards": guards
    }

    # ---------------- Thresholds ----------------
    st.sidebar.header("⚙ Thresholds")

    warning = st.sidebar.number_input("Warning threshold", min_value=1, value=10)
    critical = st.sidebar.number_input("Critical threshold", min_value=1, value=20)

    thresholds = {
        "warning": int(warning),
        "critical": int(critical)
    }

    # ---------------- Model Selection ----------------
    st.sidebar.header("🤖 Model Selection")

    model_choice = st.sidebar.selectbox(
        "Choose YOLO model",
        ["yolov8n.pt", "yolov8s.pt", "yolov8m.pt", "yolov8l.pt"],
        index=1
    )

    return source_type, video_file, rtsp_url, scene_info, thresholds, model_choice
