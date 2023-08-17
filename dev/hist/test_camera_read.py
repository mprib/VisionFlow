import cv2
import numpy as np
import platform

from pathlib import Path


if platform.system() == "Windows":
    connection_method = cv2.CAP_DSHOW
elif platform.system() == "Darwin":
    connection_method = cv2.CAP_AVFOUNDATION
elif platform.system() == "Linux":
    connection_method = cv2.CAP_MSMF
    
# Create a capture object for the webcam
capture = cv2.VideoCapture(0, connection_method)
width = 1280
height = 720
# collect a test frame
capture.set(cv2.CAP_PROP_FRAME_WIDTH, width)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
success, frame = capture.read()


# Check if the capture object was successfully opened
if not capture.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Create a server socket

while True:
    ret, frame = capture.read()
    if ret:
        print(f"A frame of size {frame.shape} is being read")
    cv2.imshow("Webcam", frame)
    
    if cv2.waitKey(1) ==ord("q"):
       cv2.destroyAllWindows()
       break

