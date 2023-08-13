import log_manager
logger = log_manager.get(__name__)

import socket
from threading import Thread

HOST_IP = socket.gethostbyname(socket.gethostname())
HOST_PORT = 12346
ENCODER = "utf-8"
BYTESIZE = 1024


# create a server socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST_IP, HOST_PORT))

def send_message():
    """
    Send a message to the server to be broadcast
    """
    message = "client-side send message thread running"
    client_socket.send(message.encode(ENCODER))
    while True:
        client_socket.send(message.encode(ENCODER))
        message = input("Message:")

def receive_message():
    """
    receive an incoming message from the server
    """
    while True:
        message = client_socket.recv(BYTESIZE).decode(ENCODER)
        client_socket.send(message.encode(ENCODER))
        logger.info(message)

send_thread = Thread(target = send_message, args=[],daemon=False)
send_thread.start()

receive_thread = Thread(target= receive_message, args=[],daemon=False)
receive_thread.start()