import socket
import hashlib
import hmac

# Function to compute HMAC with password and challenge
def compute_hmac(password, challenge):
    return hmac.new(password.encode(), challenge.encode(), hashlib.sha1).digest()

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

        if username == "johndoe" and password == "random":
            # Step 1: Send a challenge to the client
            challenge = "public_challenge" 
            conn.sendall(challenge.encode())
            
            # Step 2: Receive HMAC from client
            client_hmac = conn.recv(1024)

            # Step 3: Verify HMAC (server-side computation)
            expected_hmac = compute_hmac(password, challenge)

            if client_hmac == expected_hmac:
                conn.sendall(b"Success! You are logged in.")
            else:
                conn.sendall(b"Failure! Invalid HMAC.")
        else:
            conn.sendall(b"Failure! Invalid username or password.")
    
    conn.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()