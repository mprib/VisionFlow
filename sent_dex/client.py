import socket
import log_manager
logger = log_manager.get(__name__)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

buffer_size = 8 
data = b""

while True:
    packet = s.recv(buffer_size)
    if not packet:
        break

    data += packet

logger.info(data.decode("utf-8"))