# echo-client.py
import math
import socket
from string import whitespace

HOST = "127.0.0.1"  # The server's hostname or IP address
# The port used by the server
for PORT in range(1,65552):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print(PORT)
        connect = s.connect((HOST, PORT))
        if connect == 1:
            s.sendall(b"Hello, world")
            data = s.recv(1024)
        if connect == 0:
            print("connection failed!")

    print(f"Received {data!r}")
   