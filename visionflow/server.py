from visionflow.log_manager import get
logger = get(__name__)

import cv2
import socket
import struct
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
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host =  socket.gethostbyname(socket.gethostname())
port = 12345
server_socket.bind((host, port))
server_socket.listen(5)

print(f"Server listening on {host}:{port}")

client_socket, client_address = server_socket.accept()
print(f"Connection from: {client_address}")

while True:
    ret, frame = capture.read()

    # convert frame to bytes
    frame = frame.astype(np.uint8)  # Ensure data is of type uint8
    # Serialize the frame as bytes
    frame_bytes = frame.tobytes()
    frame_size = len(frame_bytes)
    # Get the frame shape for reconstruction
    
    frame_shape = frame.shape
    logger.info(f"Frame shape is: {frame_shape}")

    # package shape too
    header = struct.pack('<LIII', frame_size, *frame.shape)

    # combine the header and data
    message = header + frame_bytes

    # send the data over the socket
    client_socket.sendall(message) 
    

# Close the sockets and release the capture object
client_socket.close()
server_socket.close()
capture.release()
