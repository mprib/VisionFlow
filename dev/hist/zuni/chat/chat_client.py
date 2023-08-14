import socket

# define constants to be used

DEST_IP = socket.gethostbyname(socket.gethostname())
DEST_PORT = 12345
ENCODER = "utf-8"
BYTESIZE = 1024

# create a client socket and connect to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((DEST_IP,DEST_PORT))

# send and receive messages
while True:
    # receive info from server
    message = client_socket.recv(BYTESIZE).decode(ENCODER)
    if message == "quit":
    
        client_socket.send("quit".encode(ENCODER))
        print("\nEnding the chat...goodbye...")
        break
    
    print(f"\n{message}")
    message = input("Message: ")
    client_socket.send(message.encode(ENCODER)) 

# close socket if break out of while loop
client_socket.close()
    