# 📱 Missed Call Auto Messenger

A Streamlit-based Python application that helps you automatically send a custom message to a contact if you've missed their call. It includes optional scheduled messaging, making sure your responses are timely—even if you're not!

---

🚀 Features

- 📇 Enter Contact Number: Input the recipient's number (with country code).
- ✉️ Custom Message Support: Compose your own auto-reply message.
- ⏰ Scheduled Messaging: Choose to send the message immediately or after a short delay (0 to 5 minutes).
- ✅ Visual Confirmation: Displays scheduled time, success message, and message logs.
- 🎈 Interactive UI: Built with Streamlit for simplicity and ease-of-use.

---

🛠 How It Works

1. User Interface (UI) is built using Streamlit to allow input of:
   - Contact number
   - Custom message
   - Message scheduling delay (in minutes)

2. When the "Schedule & Send Message" button is clicked:
   - The system calculates the target time using datetime.now() and timedelta.
   - The program pauses execution (simulated) using time.sleep() for the specified duration.
   - Once the timer ends, a message is displayed as "Sent" with celebratory balloons.
   - A log of the message, contact number, and scheduled time is shown for reference.

Note: This is a prototype UI and does not send actual SMS. It’s designed to simulate the logic behind missed call messaging automation.

---

🧩 Components of the Code

1. streamlit Interface  
Used for creating the web interface with input fields and buttons.

2. datetime and timedelta  
Handles current time and scheduling logic for delayed messaging.

3. time.sleep()  
Simulates the passage of time for scheduling the message send.

4. User Feedback & Visualization  
- st.spinner shows a loading animation.  
- st.success, st.error, and st.balloons give feedback to the user.  
- Message logs are formatted with Markdown and shown with timestamp.

---

📦 Requirements

Install the dependencies using pip:

pip install streamlit

---

▶️ Run the App

Use the following command in your terminal:

streamlit run app.py

Replace app.py with your script filename if it's different.

---

📸 Screenshot

(Optional) Include a screenshot here if you want to showcase the UI.

---

🙋‍♂️ Author

Mayank Jangid  
Built with ❤️ for productivity and automation.

---

🌐 Future Enhancements (Optional Ideas)

- Integration with Twilio or other SMS APIs to send actual messages  
- Missed call detection via phone or VoIP services  
- Webhook or mobile app integration for real-time automation

---
