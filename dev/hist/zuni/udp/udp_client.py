import  socket

import visionflow.log_manager as log_manager
logger = log_manager.get(__name__)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# because running it on the same machine for this example
server_IP = socket.gethostbyname(socket.gethostname())
server_port = 12345

message = "Hello server!".encode('utf-8')

client_socket.sendto(message,(server_IP, server_port))