import socket

server_socket = socket.socket()
server_socket.bind(('localhost', 12347))
server_socket.listen(1)
print("Waiting for file...")

conn, addr = server_socket.accept()
filename = "received_file.txt"
with open(filename, 'wb') as f:
    while True:
        data = conn.recv(1024)
        if not data:
            break
        f.write(data)

print("File received and saved.")
conn.close()