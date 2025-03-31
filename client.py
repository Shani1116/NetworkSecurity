import socket

def start_client():
    # Client setup
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 5000))

    print("Connected to the server. Starting protocol...")

    # Authentication process
    if client_socket.recv(1024).decode() == "Hello":
        client_socket.sendall(b"Hello")
        
        if client_socket.recv(1024).decode() == "Request Username":
            client_socket.sendall(b"johndoe")  # Change this to test different usernames
        
        if client_socket.recv(1024).decode() == "Request Password":
            client_socket.sendall(b"secr3t")  # Change this to test different passwords

        response = client_socket.recv(1024).decode()
        print("Server response:", response)

    client_socket.close()

if __name__ == "__main__":
    start_client()