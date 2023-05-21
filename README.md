# Attendance-System

The Face Recognition Attendance Project is a Python-based project that uses face recognition technology to recognize faces in real-time and mark the attendance of individuals. It utilizes the OpenCV library for capturing video from a webcam, the face_recognition library for face detection and recognition, and provides functionality to send an attendance report via email.

# Features
* Real-time face detection and recognition using webcam
* Attendance tracking by marking the name and time in a CSV file
* Email integration to send the attendance report with the CSV file as an attachment

## Prerequisites
Before running the project, ensure that the following dependencies are installed:

Install all the required library in the requirement folder.
by using the command  
* pip install -r requirements.txt

# Usage
* Clone the repository or download the project files.
* Create a directory named "Training_images" in the project root directory.
* Place the training images in the "Training_images" directory. Each image should contain a single face and be named with the corresponding person's label.
* Update the email configuration in the code. Provide your sender email, sender password, receiver email, and set the subject and body for the email.
* Run the Python script main.py
* The webcam will open, and faces detected in the video stream will be recognized and marked for attendance. The name and timestamp will be stored in the Attendance.csv file.

* Once per day, the attendance report will be sent via email with the CSV file attached. The email will be sent to the provided receiver email address.



