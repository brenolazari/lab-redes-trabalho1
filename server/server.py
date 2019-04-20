import socket
from threading import Thread

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

class Thread_canal(Thread):
    def __init__ (self, nome, UDP_IP, UDP_PORT):
        Thread.__init__(self)
        self.nome = nome
        self.usuarios = []
        self.UDP_IP = UDP_IP
        self.UDP_PORT = UDP_PORT

    def add_user(self, nome):
        self.usuarios.append(nome)
        print("adicionado: " + self.usuarios[-1])
    
    def run(self):
        print("canal criado: " + self.nome)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
        sock.bind((self.UDP_IP, self.UDP_PORT))

        while True:
            data, addr = sock.recvfrom(2048) # buffer size is 1024 bytes
            print("received message:", data.decode())

def main():
    global UDP_IP
    global UDP_PORT
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
    sock.bind((UDP_IP, UDP_PORT))
    
    while True:
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        received_data = data.decode().split()
        print("received message:", received_data[1])

        if received_data[1] == "/create":
            UDP_PORT = UDP_PORT + 1
            thread_canal = Thread_canal(received_data[2], UDP_IP, UDP_PORT)
            thread_canal.start()
            thread_canal.add_user(received_data[0])

            sock.sendto("ACK tes".encode(), (UDP_IP, UDP_PORT-1))

        elif received_data[1] == "/join":
            print("join")
            # verificar se canal existe
            thread_canal.add_user(received_data[0])
        else:
            print("erro")

        # quando novo channel for criado, armazenar quem eh o admin
main()