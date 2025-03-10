import socket

IP = "127.0.0.1"
PORT = 4000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IP, PORT))
server.listen(2)
crosses, addr1 = server.accept()
noughts, addr2 = server.accept()
crosses.close()
noughts.close()
server.close()