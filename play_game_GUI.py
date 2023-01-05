
from tkinter import *

board = {}


def blank_board(label):
    count = 0
    for i in range(8):
        for j in range(8):
            board[i * 8 + j] = Button(board)
            board[i * 8 + j].grid(row = i, column = j)

root = Tk()

#myLabel = Label(root, text="minesweeper")

B = Button(root, text = " ")

B.pack()

root.mainloop()
