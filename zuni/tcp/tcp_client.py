
import  socket

import log_manager
logger = log_manager.get(__name__)

# create a client side socket that uses IPV4 (AF_INRT) and TCP (SOCK_STREAM)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# because running it on the same machine for this example
server_IP = socket.gethostbyname(socket.gethostname())
server_port = 12345

client_socket.connect((server_IP, server_port))


# receive a message from the server...you must specify the max number of bytes to receive
message = client_socket.recv(10)
logger.info(f"Message received is: {message.decode('utf-8')}")

message = client_socket.recv(10)
logger.info(f"Message received is: {message.decode('utf-8')}")

client_socket.send("this is a test. Client sends to server on same socket.".encode())

# close the client socket (best practice)
client_socket.close()