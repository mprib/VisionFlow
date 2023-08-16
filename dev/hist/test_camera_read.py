import cv2
import numpy as np

from pathlib import Path

# Create a capture object for the webcam
capture = cv2.VideoCapture(0, cv2.CAP_ANY)

# collect a test frame
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
    #cv2.imshow("Webcam", frame)
    
    #if cv2.waitKey(1) ==ord("q"):
    #    cv2.destroyAllWindows()
    #    break

