import cv2
import log_manager
logger = log_manager.get(__name__)
import time
import socket
import numpy as np
import struct
from pathlib import Path
import argparse

# Initialize ArgumentParser object
parser = argparse.ArgumentParser()

# Add host argument
parser.add_argument('-H', '--host', type=str, default='localhost',
                    help='Host IP for the server.')

args = parser.parse_args()

# Use args.host in place of the host IP
host = args.host

if __name__== "__main__":
    # for current debug and development purposes
    host = "192.168.86.42"
# Create a client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 12345
logger.info(f"Client connecting on {host}:{port}")
client_socket.connect((host, port))

def receive_all(sock, count):
    buf = b''
    while count:
        newbuf = sock.recv(count)
        if not newbuf:
            return None
        buf += newbuf
        count -= len(newbuf)
    return buf

frame_count = 0
tic = time.time()

while True:
    # Receive the header from the server
    # note it is 16 because each integer is 4 bytes and each piece of 
    # data is an integer: frame_byte_size, frame_height, frame_width, frame_channels
    header = receive_all(client_socket, 4)

    # Unpack the header to get the size and shape of the frame
    # note taht unpack will yield a tuple even if only length 1
    frame_size = struct.unpack('<L', header)[0]

    # Receive the data from the server
    frame_bytes = receive_all(client_socket, frame_size)

    # Convert bytes to numpy array
    np_array = np.frombuffer(frame_bytes, dtype=np.uint8)

    # Decode JPEG representation
    frame = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
    
    # Convert the data back to a numpy array
    frame_count += 1
    toc = time.time()
    fps = round(frame_count/(toc-tic),0)
    logger.info(f"Receiving at {fps} fps")

    cv2.imshow("Received Frame", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Close the socket and destroy OpenCV windows
client_socket.close()
cv2.destroyAllWindows()
