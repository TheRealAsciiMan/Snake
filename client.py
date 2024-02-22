import socket

posx = 8
posy = 9

sending_port = 15
sending_ip = input("Veuillez rentrer l'adresse IPv4 de l'autre joueur (Ex: 192.168.0.127) : ")
if sending_ip == "":
    sending_ip = "127.0.0.1"
sSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sSocket.connect((sending_ip, sending_port))
    print("Client connecté")

    sData = str([posx, posy])
    sData = sData.encode("utf8")
    sSocket.sendall(sData)
except:
    print("Connexion échouée")

sSocket.close()