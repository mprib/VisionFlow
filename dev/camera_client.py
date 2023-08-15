import cv2
import socket
import numpy as np
import struct
from pathlib import Path

# Create a client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'  # Change this to the server's IP address
port = 12345
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


while True:
    # Receive the header from the server
    # note it is 16 because each integer is 4 bytes and each piece of 
    # data is an integer: frame_byte_size, frame_height, frame_width, frame_channels
    header = receive_all(client_socket, 16)

    # Unpack the header to get the size and shape of the frame
    frame_size, height, width, channels = struct.unpack('<LIII', header)

    # Receive the data from the server
    frame_bytes = receive_all(client_socket, frame_size)
    # Convert the data back to a numpy array
    frame = np.frombuffer(frame_bytes, dtype=np.uint8).reshape((height, width, channels))

    cv2.imshow("Received Frame", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Close the socket and destroy OpenCV windows
client_socket.close()
cv2.destroyAllWindows()
