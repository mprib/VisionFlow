import socket
import log_manager
logger = log_manager.get(__name__)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

buffer_size = 8 

while True:
    msg = s.recv(buffer_size)
    print(msg.decode("utf-8"))
    logger.info(msg.decode("utf-8"))