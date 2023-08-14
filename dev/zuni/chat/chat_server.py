# chat server side

import socket

# define constants
HOST_IP = socket.gethostbyname(socket.gethostname())
HOST_PORT = 12345
ENCODER = "utf-8"
BYTESIZE = 1024

# Create server socket [IPv4 and TCP]
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST_IP, HOST_PORT))
server_socket.listen()

# accept any incoming connection and let them know they are connected
print("Server is running...\n")
client_socket, client_address = server_socket.accept()

client_socket.send("You are connected to the server...\n".encode(ENCODER))

while True:
    # receive information from the client
    message = client_socket.recv(BYTESIZE).decode(ENCODER)
    if message == "quit":
        client_socket.send("quit".encode(ENCODER))
        print("Ending the chat...goodbye")
        break

    print(f"\n{message}")
    message = input("Message: ")
    client_socket.send(message.encode(ENCODER))