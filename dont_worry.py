import streamlit as st
from datetime import datetime, timedelta
import time

# Set page config
st.set_page_config(page_title="Missed Call Auto Messenger", page_icon="📱", layout="centered")

# Title and description
st.title("📱 Don't Worry!")
st.subheader("Missed Call Auto-Messenger")
st.markdown(
    """
    This application helps you automatically send a **custom message** to your contacts when you miss their call.

    Now with 💡 **Scheduled Messaging** support!
    """
)

# Input fields
contact_number = st.text_input("📇 Enter Contact Number", placeholder="e.g. +91XXXXXXXXXX")
custom_message = st.text_area("✉️ Enter Custom Message", placeholder="e.g. Hey! I missed your call. Will get back soon.")

# Time delay options
delay_minutes = st.selectbox("⏰ Schedule Message After:", [0, 1, 2, 5], index=0, format_func=lambda x: f"{x} minute(s)")

# Simulate send action
if st.button("📤 Schedule & Send Message"):
    if contact_number and custom_message:
        current_time = datetime.now()
        scheduled_time = current_time + timedelta(minutes=delay_minutes)

        st.markdown(f"🕒 Message scheduled for **{scheduled_time.strftime('%Y-%m-%d %H:%M:%S')}**")

        with st.spinner("Waiting to send message..."):
            time.sleep(delay_minutes * 60)  # delay in seconds

        st.success("✅ Message Sent!!")
        st.balloons()

        # Display log
        st.markdown("---")
        st.subheader("📜 Message Log")
        st.markdown(f"**To:** `{contact_number}`  \n**Message:** `{custom_message}`  \n**Scheduled At:** `{scheduled_time.strftime('%Y-%m-%d %H:%M:%S')}`")
    else:
        st.error("⚠️ Please enter both contact number and message.")
