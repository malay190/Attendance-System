import cv2
import numpy as np
import face_recognition

ali_image = face_recognition.load_image_file("imagebasics/navneet.jpeg")
imgAli = cv2.cvtColor(ali_image, cv2.COLOR_BGR2RGB)

#cv2.imshow("Ali",ali_image)
cv2.imshow("Ali",imgAli)

faceLocTest = face_recognition.face_locations(imgAli)[0]
encode = face_recognition.face_encodings(imgAli)[0]
cv2.rectangle(imgAli,(faceLocTest[3],faceLocTest[0]),(faceLocTest[1],faceLocTest[2]), (255,0,55),2)

results = face_recognition.compare
cv2.waitKey(0)
 