import socket
import threading

class ChatServer:
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(("127.0.0.1", 12345))
        self.server.listen(5)
        self.clients = []

    def broadcast(self, message, client_socket):
        for client in self.clients:
            if client != client_socket:
                try:
                    client.send(message)
                except:
                    self.clients.remove(client)

    def handle_client(self, client_socket):
        while True:
            try:
                message = client_socket.recv(1024)
                if message:
                    self.broadcast(message, client_socket)
            except:
                self.clients.remove(client_socket)
                break

    def start(self):
        print("Server started...")
        while True:
            client_socket, client_address = self.server.accept()
            self.clients.append(client_socket)
            print(f"Client connected: {client_address}")
            threading.Thread(target=self.handle_client, args=(client_socket,)).start()

class ChatClient:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(("127.0.0.1", 12345))

    def send_message(self, message):
        self.client.send(message.encode())

    def receive_message(self):
        while True:
            message = self.client.recv(1024).decode()
            print(message)

    def start(self):
        threading.Thread(target=self.receive_message).start()
        while True:
            message = input()
            self.send_message(message)

if __name__ == "__main__":
    choice = input("1. Start Server\n2. Start Client\nChoose: ")
    if choice == "1":
        server = ChatServer()
        server.start()
    elif choice == "2":
        client = ChatClient()
        client.start()
