import socket
import log_manager
logger = log_manager.get(__name__)
import time

# create a server side socket using IPV4 (AF_INET) and TCP (SOCK_STREAM)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
