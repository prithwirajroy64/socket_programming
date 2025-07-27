import socket

client_socket = socket.socket()
client_socket.connect(('localhost', 12347))
filename = input("Enter file path to send: ")

with open(filename, 'rb') as f:
    data = f.read(1024)
    while data:
        client_socket.send(data)
        data = f.read(1024)

print("File sent successfully.")
client_socket.close()