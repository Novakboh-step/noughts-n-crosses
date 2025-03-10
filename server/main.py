import socket

IP = "127.0.0.1"
PORT = 4000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IP, PORT))
server.listen(2)
conn1, addr1 = server.accept()
conn2, addr2 = server.accept()
conn1.close()
conn2.close()
server.close()