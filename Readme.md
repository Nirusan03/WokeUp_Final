# Elder Guardian

## Overview
Elder Guardian is a **real-time video and audio analysis application** designed to ensure the safety of elderly individuals. The system uses **pose detection**, **motion sensing**, and **audio recognition** to monitor seniors and send alerts in case of emergencies (e.g., falls, distress signals). 

The project consists of:
- **Flask Web Application** – Backend system with MongoDB for storing user data and OpenCV-based real-time video streaming.
- **Flutter Mobile Application** – Cross-platform mobile app for real-time monitoring, notifications, and alerts.

---

## Features
✅ Real-time **video streaming** using OpenCV  
✅ **Fall detection** using Pose Detection Algorithms  
✅ **Automated email alerts** in case of emergencies  
✅ **Secure user authentication** (Signup/Login with MongoDB)  
✅ **Mobile application for remote monitoring**  
✅ **Intuitive UI** with Flask + HTML + CSS + Flutter  

---

## Setup Guide
### **1. System Requirements**
- **Python 3.10+**
- **Flask**
- **MongoDB** (Local or Cloud-based)
- **OpenCV** (`cv2`)
- **Pose Detector** (`cvzone`)
- **Flutter SDK** (for mobile app development)

### **2. Clone the Repository**
```sh
# Clone the project
git clone https://github.com/your-repo/ElderGuardian.git
cd ElderGuardian
```

---

## Flask Backend Setup
### **1. Create a Virtual Environment**
```sh
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### **2. Install Dependencies**
```sh
pip install -r requirements.txt
```

### **3. Run MongoDB Locally (Optional)**
Ensure MongoDB is running:
```sh
mongod --dbpath /your/mongo/data/path
```

### **4. Start the Flask Server**
```sh
python app.py
```
**Backend Runs at:** `http://127.0.0.1:5000/`

---

## Frontend (Flask Web UI)
The Flask server serves the following pages:
- **`/signup1`** – User Registration Step 1
- **`/signup2`** – User Registration Step 2
- **`/home`** – Dashboard for real-time monitoring
- **`/stream`** – Video streaming interface

Run Flask and visit `http://127.0.0.1:5000/` in your browser.

---

## Flutter Mobile Application
### **1. Install Flutter Dependencies**
```sh
cd Flutter_Dev
flutter pub get
```

### **2. Run the Flutter Application**
```sh
flutter run
```

This will launch the mobile app on a connected device or emulator.

---

## How It Works
### **1. Elder Monitoring System**
- A **360-degree video monitoring robot** (or a mobile device) records the elder’s environment.
- **Pose Detection Algorithm** identifies falls or unusual postures.
- **Audio Analysis** detects distress calls.
- If an anomaly is detected, an **alert notification** is sent to the registered caregiver.

### **2. Fall Detection Algorithm**
- Uses **OpenCV + Pose Detection** to analyze human posture.
- If the person is detected as **laying down for too long**, an alert is triggered.
- An **email alert is sent** to the caregiver.

### **3. Secure Authentication**
- User data is stored in **MongoDB**.
- Authentication system for **caregivers & elders**.
- Real-time alerts & monitoring via **Flask Web App & Flutter Mobile App**.

---

## API Endpoints
| Endpoint         | Method | Description |
|-----------------|--------|-------------|
| `/signup1`      | GET    | Signup Page |
| `/signup2`      | GET    | Next Signup Step |
| `/home`         | GET    | Dashboard |
| `/stream`       | GET    | Video Stream Page |
| `/video_feed`   | GET    | Returns real-time video stream |

---

## Security Considerations
🔒 **Data Privacy:** Uses **MongoDB** with **secure authentication**.  
🔒 **No Public Servers:** Stores sensitive video/audio only on **private servers**.  
🔒 **Encryption:** Ensures **secure email notifications** for alerts.  

---

## Future Enhancements
🚀 **Integration with Smart Home Systems**  
🚀 **AI-based Health Pattern Analysis**  
🚀 **Cloud-based Video Storage**  
🚀 **Voice Assistant Integration**  

---

## Contributors
👨‍💻 **Nirusan Hariharan**  
👨‍💻 **Arfith Ahamed**  
👨‍💻 **Jaiyramanan Vijayaalayan**  
👨‍💻 **Rishimithun Muralidharan**  

📧 For inquiries, contact: **nirusan.hariharan350@gmail.com**  

---

## License
📜 This project is licensed under the **MIT License**. Feel free to use and modify it!
