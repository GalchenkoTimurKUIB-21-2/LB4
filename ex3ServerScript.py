import socket
from datetime import datetime

HOST = ''
PORT = 50007


def generate_unique_filename(base_name="received_file"):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{base_name}_{timestamp}.txt"


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(5)
    print("Server is running and waiting for connections...")

    while True:
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)

            original_filename = conn.recv(1024).decode()
            print(f"Receiving file: {original_filename}")

            unique_filename = generate_unique_filename()
            print(f"Saving file as: {unique_filename}")

            while True:
                text = conn.recv(1024)

                if not text:
                    break

                data = text.decode('utf-8')

                if data == "END_OF_TRANSFER":
                    break

                with open(unique_filename, 'w', encoding='utf-8') as file:
                    file.write(data)

                print(f"File {unique_filename} has been saved successfully.")

            conn.sendall(b"File received and saved.")
