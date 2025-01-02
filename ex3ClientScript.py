import socket

HOST = 'localhost'
PORT = 50007

filename = 'example.txt'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    s.sendall(filename.encode('utf-8'))

    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

        for line in lines:
            s.sendall(line.encode('utf-8'))

    s.sendall(b"END_OF_TRANSFER")

    data = s.recv(1024)
    print('Received', repr(data.decode('utf-8')))
