# UDP Server side

import  socket

import log_manager
logger = log_manager.get(__name__)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# because running it on the same machine for this example
server_IP = socket.gethostbyname(socket.gethostname())
server_port = 12345

server_socket.bind((server_IP, server_port))

message, address = server_socket.recvfrom(1024)
logger.info(message.decode('utf-8'))
logger.info(address)