import socket
import log_manager
logger = log_manager.get(__name__)
import time

# create a server side socket using IPV4 (AF_INET) and TCP (SOCK_STREAM)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# see how to get IP address dynamically
server_IP = socket.gethostbyname(socket.gethostname())
server_port = 12345
logger.info(f"creating server at {server_IP}")

# bind our new socket to a tuple (IP Address, Port Address)
server_socket.bind((server_IP, server_port))

# put the socket into listening mode to be on the lookout for connections
server_socket.listen()
loops = 0 
# listen forever to accept any connection
while True:
    # accept every connection and store socket, address
    client_socket, client_address = server_socket.accept()
    logger.info(f"Client socket type is {type(client_socket)}")
    logger.info(f"Client socket is {client_socket}")
    logger.info(f"client address is type: {type(client_address)}")
    logger.info(f"Client address is {client_address}")
    loops +=1
    logger.info(f"{loops} time(s) through the loop")

    # send a message to the client 
    client_socket.send("Connection successful!".encode("utf-8"))
    msg = client_socket.recv(1024)
    logger.info(msg.decode())
    client_socket.close()
    break
