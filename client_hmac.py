import socket
import hashlib
import hmac

USERNAME = "USERNAME"
PASSWORD = "PASSWORD"

# Function to compute HMAC with password and challenge
def compute_hmac(password, challenge):
    return hmac.new(password.encode(), challenge.encode(), hashlib.sha1).digest()

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 5000))

    # Step 1: Send "Hello" to the server
    client_socket.sendall(b"Hello")

    # Step 2: Receive request for username and send hardcoded username
    username_request = client_socket.recv(1024)
    print(username_request.decode())
    client_socket.sendall(USERNAME.encode())

    # Step 3: Receive request for password and send hardcoded password
    password_request = client_socket.recv(1024)
    print(password_request.decode())
    client_socket.sendall(PASSWORD.encode())

    # Step 4: Receive challenge from the server
    challenge = client_socket.recv(1024).decode()
    print(f"Received challenge: {challenge}")

    # Step 5: Compute HMAC with password and challenge
    hmac_response = compute_hmac(PASSWORD, challenge)
    print(f"Sending HMAC response: {hmac_response}")
    client_socket.sendall(hmac_response)

    # Step 6: Receive success or failure message from the server
    result = client_socket.recv(1024)
    print(f"Server response: {result.decode()}")

    client_socket.close()

if __name__ == "__main__":
    start_client()
