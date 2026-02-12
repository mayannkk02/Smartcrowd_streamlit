import streamlit as st
import cv2

def show_video_frame(frame_placeholder, frame):
    """Render a single video frame in Streamlit."""
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame_placeholder.image(frame_rgb, channels="RGB")

def show_metrics(metrics_placeholder, count, avg_count, density):
    """Display live crowd metrics."""
    with metrics_placeholder:
        col1, col2, col3 = st.columns(3)
        col1.metric("👥 Current Count", count)
        col2.metric("📈 Avg (last 30s)", f"{avg_count:.1f}")
        col3.metric("🧮 Density (approx.)", f"{density:.2f} people/m²")

def show_alert(alert_placeholder, status, suggestion):
    """Show alert banners with messages."""
    if status == "CRITICAL":
        alert_placeholder.error(f"🚨 CRITICAL: {suggestion}")
    elif status == "WARNING":
        alert_placeholder.warning(f"⚠️ Warning: {suggestion}")
    else:
        alert_placeholder.success("✅ Normal: Safe crowd level")
