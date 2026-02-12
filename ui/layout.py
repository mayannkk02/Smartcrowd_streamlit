import streamlit as st

def setup_page():
    """Set up page configuration and header for SmartCrowd."""
    st.set_page_config(
        page_title="SmartCrowd Monitoring",
        page_icon="🚦",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    st.title("🚦 SmartCrowd Monitoring System")
    st.markdown("---")
