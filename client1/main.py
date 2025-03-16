import socket
from tkinter import *

class Cell:
    def __init__(self, x, y):
        self.__coordinates = f"{x},{y}"
        self.__button = Button(width=13, height=6, command=self.changeSign)
        self.__button.grid(row=y+1, column=x)

    def changeSign(self):
        self.__button.config(text=sign, state=DISABLED)
        client.send(self.__coordinates.encode())
        turnLabel.config("Opponent`s turn")

IP = "127.0.0.1"
PORT = 4000
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((IP, PORT))
sign = client.recv(1024).decode()
root = Tk()
root.geometry("300x400")
root.title("Noughts and crosses")
turnLabel = Label(text=client.recv(1024).decode())
turnLabel.grid(row=0, column=0, columnspan=3)
field = [
    [
        Cell(0, 0),
        Cell(1, 0),
        Cell(2, 0)
    ],
    [
        Cell(0, 1),
        Cell(1, 1),
        Cell(2, 1)
    ],
    [
        Cell(0, 2),
        Cell(1, 2),
        Cell(2, 2)
    ]
]
root.mainloop()
client.close()