from tkinter import *

class Game:
    def __init__(self, sign):
        self.__sign = sign
        self.__root = Tk()
        self.__root.geometry("300x300")
        self.__root.title("Noughts and crosses")
        self.__field = [
            [
                Button(command=self.__changeSign),
                Button(command=self.__changeSign),
                Button(command=self.__changeSign)
            ],
            [
                Button(command=self.__changeSign),
                Button(command=self.__changeSign),
                Button(command=self.__changeSign)
            ],
            [
                Button(command=self.__changeSign),
                Button(command=self.__changeSign),
                Button(command=self.__changeSign)
            ]
        ]
        for i in range(3):
            for j in range(3):
                self.__field[i][j].grid(row=i, column=j)

    def __changeSign(self):