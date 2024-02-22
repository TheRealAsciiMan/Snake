import socket

listening_port = 15

lSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lSocket.bind(('', listening_port))

lSocket.listen(1)
conn, adress = lSocket.accept()
print("Un client vient de se connecter")
lData = conn.recv(1024)
lData = lData.decode("utf8")
lData = eval(lData)

conn.close()
lSocket.close()