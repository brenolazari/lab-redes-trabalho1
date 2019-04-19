import sys, os
import socket

class Usuario:
    def __init__(self):
        self.nickname = ""

def printa_comandos():
    print(":: Comandos ::")
    print("/nick <nickname>")
    print("/create <channel>")
    print("/remove <channel>")
    print("/list ")
    print("/join <channel>")
    print("/part ")
    print("/names ")
    print("/kick <channel> <nickname>")
    print("/msg <nickname> <message>")
    print("/<message>")
    print("/help")
    print("/quit\n")

def main():
    # inicio
    print("Bem vindo ao 'mIRC' do Trabalho 1 de Lab. Redes!\n")
    printa_comandos()

    # configuracao socket 
    UDP_IP = "127.0.0.1"
    UDP_PORT = 5005
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP

    # novo usuario
    usuario = Usuario()

    # TODO: verificar se comandos tao 100% certos
    while True:
        cmd = input(">")

        if cmd == "/help":
            printa_comandos()
        elif cmd.startswith("/nick"):
            try:
                nickname = cmd.split()[1]
                usuario.nickname = nickname
                print("Novo nickname: " + usuario.nickname)
            except:
                print("Digite um comando valido!")
        elif cmd.startswith("/create"):
            print("criar channel no server")
            sock.sendto(usuario.nickname.encode(), (UDP_IP, UDP_PORT))
        elif cmd.startswith("/remove"):
            print("deletar channel do server")
        elif cmd == "list":
            print("lista canais do servidor")
        elif cmd.startswith("/join"):
            print("solicita a participacao em um canal")
        else:
            print("Digite um comando valido!")

    
    #sock.sendto(MESSAGE.encode(), (UDP_IP, UDP_PORT))

main()

