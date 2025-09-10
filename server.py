import socket

def start_server():
    # Server setup
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 5000))
    server_socket.listen(1)

    print("Server is listening...")

    conn, addr = server_socket.accept()
    print(f"Connection established with {addr}")

    # Authentication process
    conn.sendall(b"Hello")
    if conn.recv(1024).decode() == "Hello":
        conn.sendall(b"Request Username")
        username = conn.recv(1024).decode()
        
        conn.sendall(b"Request Password")
        password = conn.recv(1024).decode()
        
        # Simple authentication check
        if username == "USERNAME" and password == "PASSWORD5:
            conn.sendall(b"Success! You are logged in.")
        else:
            conn.sendall(b"Failure! Invalid username or password.")

    conn.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()
