import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_address = ('127.0.0.1', 5555)
server_socket.bind(server_address)

# Listen for incoming connections (max 5 connections in the queue)
server_socket.listen(5)

print(f"Server is listening on {server_address}")

while True:
    # Wait for a connection
    client_socket, client_address = server_socket.accept()
    print(f"Received connection from {client_address}")

    # Send a welcome message to the client
    message = "Welcome to the server!"
    client_socket.send(message.encode('utf-8'))

    # Close the connection
    client_socket.close()
