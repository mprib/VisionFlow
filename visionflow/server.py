from visionflow.log_manager import get
logger = get(__name__)

import cv2
import time
import socket
import struct
import numpy as np

from pathlib import Path
import argparse
import platform

TARGET_HEIGHT = 300  # The target height you want for your image
COMPRESSION = 90
# Initialize ArgumentParser object
parser = argparse.ArgumentParser()

# Add host argument
parser.add_argument('-H', '--host', type=str, default='localhost',
                    help='Host IP for the server.')

args = parser.parse_args()

# Use args.host in place of the host IP
host = args.host
logger.info(f"Binding host to {host}")
# Create a capture object for the webcam
if platform.system() == "Windows":
    connection_method = cv2.CAP_DSHOW
else:
    connection_method = cv2.CAP_ANY

# Create a capture object for the webcam
capture = cv2.VideoCapture(0, connection_method)
width = 1280
height = 720
capture.set(cv2.CAP_PROP_FRAME_WIDTH, width)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

# collect a test frame
success, frame = capture.read()

# Check if the capture object was successfully opened
if not capture.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Create a server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 12345
server_socket.bind((host, port))
server_socket.listen(5)

print(f"Server listening on {host}:{port}")

client_socket, client_address = server_socket.accept()
print(f"Connection from: {client_address}")
frame_count = 0
tic = time.time()
while True:
    ret, frame = capture.read()
    # resize frame to fit target height
    original_frame_height, original_frame_width = frame.shape[:2]
    resize_ratio = TARGET_HEIGHT / original_frame_height

    width = int(original_frame_width * resize_ratio)
    height = int(original_frame_height * resize_ratio)

    # resizing the frame
    frame = cv2.resize(frame, (width, height), interpolation = cv2.INTER_LINEAR)
   
    # Compress the frame to JPEG
    ret, frame = cv2.imencode('.jpg', frame, [int(cv2.IMWRITE_JPEG_QUALITY), COMPRESSION])

    # ensure it's in byte format
    if not ret:
        raise Exception("Could not encode image!")
    frame_bytes = frame.tobytes()  
    

    frame_count +=1
    toc=time.time()
    fps = round(frame_count/(toc-tic),0)


    frame_size = len(frame_bytes)
    # Get the frame shape for reconstruction
    frame_shape = frame.shape
    logger.info(f"Frame shape is ({original_frame_width}, {original_frame_height})...reading on average at {fps} fps")
     
    # package shape too
    header = struct.pack('<L', frame_size)

    # combine the header and data
    message = header + frame_bytes

    # send the data over the socket
    try:
        client_socket.sendall(message) 
    except ConnectionResetError:
        logger.info(f"Client has disconnected. Shutting server down.")
        break
    

# Close the sockets and release the capture object
client_socket.close()
server_socket.close()
capture.release()
