import socket

# Define the host and port
SERVER_HOST = '192.168.30.73'  # Listen on all interfaces
SERVER_PORT = 8000

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Set socket options
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Bind the socket to the address and port
server_socket.bind((SERVER_HOST, SERVER_PORT))
# Make the socket listen for incoming connections
server_socket.listen(5)

print(f'Listening on {SERVER_HOST}:{SERVER_PORT} ...')

while True:
    # Accept incoming client connection
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address}")

    try:
        # Receive data from the client
        request = client_socket.recv(1024).decode('utf-8', errors='ignore')
        print(request)

        # Ensure that the request is an HTTP request
        if request.startswith('GET'):
            # Respond with a simple HTTP response
            response = """\
HTTP/1.1 200 OK

What is Socket Programming?
Socket programming is a way of connecting two nodes on a network to communicate with each other. 
One socket(node) listens on a particular port at an IP, while the other socket reaches out to the other to form a connection. The server forms the listener socket while the client reaches out to the server.
"""
            client_socket.sendall(response.encode('utf-8'))
        else:
            print("Received non-HTTP request")

    except Exception as e:
        print(f"Error: {e}")
    
    finally:
        client_socket.close()
