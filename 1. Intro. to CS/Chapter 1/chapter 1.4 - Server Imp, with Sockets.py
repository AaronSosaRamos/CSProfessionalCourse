import socket

# Define host and port
HOST = '127.0.0.1'
PORT = 12345

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the host and port
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen(5)

print(f"Server listening on {HOST}:{PORT}")

while True:
    # Accept incoming connection
    client_socket, addr = server_socket.accept()
    print(f"Connected to {addr[0]}:{addr[1]}")

    # Receive data from the client
    data = client_socket.recv(1024).decode('utf-8')
    print(f"Received data: {data}")

    # Echo back the received data
    client_socket.sendall(data.encode('utf-8'))

    # Close the connection
    client_socket.close()
