# server side chat room
import visionflow.log_manager as log_manager
logger = log_manager.get(__name__)

import socket
from threading import Thread

HOST_IP = socket.gethostbyname(socket.gethostname())
HOST_PORT = 12346
ENCODER = "utf-8"
BYTESIZE = 1024


# create a server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST_IP, HOST_PORT))
server_socket.listen()

# Store client sockets

sockets = {}

def broadcast_message(source, message):
    """
    Send a message to all clients connected to the server
    """
    logger.info(f"Broadcasting message")
    for address, socket in sockets.items():
        encoded_message = (f"{source[1]}: {message}").encode(ENCODER)
        socket.send(encoded_message)

def receive_message(address:str, client_socket:socket.socket):
    """
    receive an incoming message from a specific client and forward the message to be broadcast
    """
    while True:
        msg = client_socket.recv(BYTESIZE).decode(ENCODER)
        logger.info(msg)
        broadcast_message(address, msg)

def connect_clients():
    """
    connect an incoming client to the server
    """ 
    logger.info(f"Server client connection thread up and running")

    while True:
        # accept every connection and store socket, address
        client_socket, client_address = server_socket.accept()
        logger.info(f"Client socket type is {type(client_socket)}")
        logger.info(f"Client socket is {client_socket}")
        logger.info(f"client address is type: {type(client_address)}")
        logger.info(f"Client address is {client_address}")
        
        # send a message to the client 
        client_socket.send("Connection successful!".encode("utf-8"))
        sockets[client_address] = client_socket

        # establish thread that will receive incoming from this socket and broadcast out
        receive_thread = Thread(target=receive_message, args=[client_address, client_socket], daemon=False)
        receive_thread.start()
    
connect_clients_thread = Thread(target=connect_clients, args=[], daemon=False)
connect_clients_thread.start()


