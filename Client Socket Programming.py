import socket

# Set the server address and port
HOST = 'izani.synology.me'
PORT = 8443

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    try:
        sock.connect((HOST, PORT))
        # Send the UiTM student ID
        student_id = input("Enter your UiTM Student ID: ")
        data = student_id.encode('utf-8')
        sock.sendall(data)

        # Read the server response
        response = sock.recv(1024).decode('utf-8')
        print(response)
        url = response.split()[-1]  # Assuming the URL is the last word in the response
        print("Unique URL:", url)
    except ConnectionRefusedError:

        # Attempt connection
        print("Connection refused. Check server availability.")
        exit()  # Exit gracefully if connection fails

# Close the socket
sock.close()
