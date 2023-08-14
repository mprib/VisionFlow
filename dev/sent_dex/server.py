import socket
import visionflow.log_manager as log_manager
logger = log_manager.get(__name__)
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))

# listen for connections
# leave a queue of 5
s.listen(5)
counter = 0
while True:
    logger.info(f"Listening for loop {counter}...")
    connection, client_address = s.accept()
    logger.info(f"Connection from {client_address} has been established")
    connection.send(bytes("Welcome to the server", "utf-8"))
    
    counter +=1

    while True:
        time.sleep(.5)
        connection.send(bytes(f"The time is now {time.time()}", "utf-8"))
    