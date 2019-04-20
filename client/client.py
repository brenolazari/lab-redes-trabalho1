import sys, os
import socket

class Usuario:
    def __init__(self):
        self.nickname = ""
        self.joined = False
        self.channel_name = ""
        self.channel_ip = ""
        self.channel_port = 0

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

    # configuracao socket do servidor
    UDP_IP = "127.0.0.1"
    UDP_PORT = 5005
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
    msg = ""

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
            msg = usuario.nickname + " " + cmd
            sock.sendto(msg.encode(), (UDP_IP, UDP_PORT))

            # ver como enviar resposta para o cliente
            #while True:
            #    data, addr = sock.recvfrom(1024)
            #    print(data)
            #    if data != null:
            #        print("break")
            #        break

            usuario.joined = True
            usuario.channel_name = cmd.split()[1]
            usuario.channel_port = 5006 # trocar dps
        elif cmd.startswith("/remove"):
            print("deletar channel do server")
        elif cmd == "/list":
            print("lista canais do servidor")
        elif cmd.startswith("/join"):
            print("solicita a participacao em um canal")
            msg = usuario.nickname + " " + cmd
            sock.sendto(msg.encode(), (UDP_IP, UDP_PORT))
            usuario.joined = True
            usuario.channel_name = cmd.split()[1]
            usuario.channel_port = 5006 # trocar dps
        elif cmd == "/part":
            print("sair do canal")
        elif cmd == "/names":
            print("lista usuarios")
        elif cmd.startswith("/kick"):
            print("kicka")
        elif cmd.startswith("/msg"):
            print("msg priv")
        elif cmd == "/quit":
            resp = input("Tem certeza que deseja sair? (s/n): ")
            if resp.lower() == "s":

                # TODO: remover usuario do canal se for o caso
                return
        else:
            if usuario.joined == True:
                print("enviar mensagem para canal")
                msg = usuario.nickname + " " + usuario.channel_name + " " + cmd
                print(msg)
                sock.sendto(msg.encode(), (UDP_IP, usuario.channel_port))
            else:
                print("Digite um comando valido!")

main()

