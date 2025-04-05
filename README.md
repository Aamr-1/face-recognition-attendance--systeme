# Face Recognition Attendance System

## Overview
This project is a simple Face Recognition-based Attendance System. It utilizes the `face_recognition` library to recognize and register students' faces. When a student faces the camera, the system will attempt to recognize them. If recognized, their attendance is marked; if not, they will be prompted to register by providing their name, and their face will be saved for future recognition.

## Features
- Registers new students by capturing their face images.
- Compares captured faces with registered ones to mark attendance.
- Logs the attendance with timestamps in a CSV file.
- Allows students to register their face if not already registered.

## Technologies Used
- **Python**: Programming language for building the system.
- **OpenCV**: Library for capturing images and working with video.
- **Face Recognition**: Library for recognizing faces.
- **NumPy**: Used for handling image data.
- **CSV**: To store attendance records.
- **Datetime**: For timestamping attendance entries.

## Installation
Before running the project, make sure to install the required dependencies. Use `pip` to install the necessary libraries:

```bash
pip install opencv-python numpy face_recognition
```
-**opencv-python**: For capturing video and working with images.
-**numpy**: For handling arrays and image data.
-**face_recognition**: For detecting and recognizing faces.
## file structure 















