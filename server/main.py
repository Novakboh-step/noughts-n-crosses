import socket

IP = "127.0.0.1"
PORT = 4000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IP, PORT))
server.listen(2)
crosses, addr1 = server.accept()
noughts, addr2 = server.accept()
crosses.send("x".encode())
noughts.send("o".encode())
turns = ["Your turn!", "Opponent`s turn!"]
crosses.send(turns[0].encode())
noughts.send(turns[1].encode())
crosses.close()
noughts.close()
server.close()