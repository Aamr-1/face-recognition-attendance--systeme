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
![Image](https://github.com/user-attachments/assets/28729e40-24db-4a81-bcf2-1742c9133d1d)


## How the System Works
  ### Loading Registered Faces:
     
 -The system loads images from the students_images/ directory.
 -It extracts face encodings (unique identifiers for faces) from each image.
 -It keeps track of these encodings and their associated names.
 ### Capturing a Student's Face:
 -The program opens the webcam and waits for the student to appear in front of the camera.
 -The student must press the "q" key to capture their face.
### Face Recognition:
-The system attempts to match the captured face with the faces in the registered list (students_images/).
-If a match is found, the system logs the attendance (name and timestamp) in a CSV file (attendance.csv).
-If no match is found, the system will prompt the user to register their face.

### Registering a New Student:
-If a student's face is not recognized, they can register by typing their name.
-The system captures the student's face and saves it in the students_images/ directory for future recognition.

### Attendance Logging:
-Once a student is recognized, their attendance is logged in the attendance.csv file with the timestamp.

## running the program:
 #### To run the program, execute the following command in your terminal:
```bash
python face_recognition_attendance.py

```
## Process Overview:
  -The program first loads all the known faces from the students_images/ directory.
  -It then starts the webcam and waits for the student to appear.
  -If the student is recognized, their attendance is marked.
  -if  the student is not recognized, they are prompted to register.
  -Once the student registers, their face is stored, and future recognition will be possible.
## Attendance Logging:
 -The attendance is stored in a CSV file (attendance.csv) with the following format:
 ```
student_name,timestamp
e.g., Aamr_elbelamachi,2025-04-05 14:30:00


```
## Important Notes:
-The students_images/ folder must contain images of the students you want to register. The images should be named using the student's name (e.g., Aamr_elbelamachi.jpg).
-Ensure that your camera is properly connected and functional before running the script.
-Press the "q" key to capture the student's image in the webcam view.
-If you want to stop the webcam at any time, you can forcefully close the window or end the script.

## Improvements & Future Enhancements:
-Error Handling: Improve the system to handle cases where the camera is not found or no face is detected in a more user-friendly way.
-Multiple Face Detection: Enable the system to recognize multiple faces in a single frame.
-Graphical User Interface (GUI): Implement a GUI using customTkinter or PyQt to make the system more user-friendly.
-Face Database: Integrate a database to manage student records, attendance, and images efficiently.

## Conclusion
This face recognition-based attendance system provides a simple and efficient way to track student attendance without manual effort. By leveraging the power of the face_recognition library and computer vision, the system automatically recognizes students and logs their attendance.
 
















