from base64 import b16decode
from binascii import a2b_base64
from tkinter import *

root = Tk()
root.title("Tic Tac Toe application")
root.geometry("500x500")

turn = "X"
isWinner = 0

computer = "X"
player = "O"

board = {"a1":" ", "b1":" ","c1":" ",
        "a2":" ","b2":" ","c2":" ",
        "a3":" ","b3":" ","c3":" "}


def updateBoard(board):
    for key, value in board.items():
        tracker[key]["text"] = value

positions = []
for i in board.keys():
    positions.append(i)

def compMove():
    global turn
    bestScore = -100
    for key in board.keys():
        if board[key] == " ":
            board[key] = "O"
            score = miniMax(board,False)
            board[key] = " "
            if score > bestScore:
                bestScore = score
                bestKey = key
    insert("O",bestKey)
    updateBoard(board)
    print(bestKey)
    turn = "X"

def miniMax(board,isMaximising):
    if chfowin(computer): 
        return(-1)
    elif chfowin(player): 
        return(1)
    elif chfodra(): 
        return(0)
    
    if isMaximising:
        bestScore = -100
        for key in board.keys():
            if board[key] == " ":
                board[key] = "O"
                score = miniMax(board,False)
                board[key] = " "
                if score > bestScore:
                    bestScore = score
        return bestScore
    else:
        bestScore = 100
        for key in board.keys():
            if board[key] == " ":
                board[key] = "X"
                score = miniMax(board,True)
                board[key] = " "
                if score < bestScore:
                    bestScore = score
        return bestScore
            


def play(event):
    global turn
    if isWinner == 1:
        return
    selected = event.widget
    strSelected = str(selected)
    position = ""
    if strSelected[-1] == "n":
        position = "a1"
    elif strSelected[-1] == "2":
        position = "a2"
    elif strSelected[-1] == "3":
        position = "a3"
    elif strSelected[-1] == "4":
        position = "b1"
    elif strSelected[-1] == "5":
        position = "b2"
    elif strSelected[-1] == "6":
        position = "b3"
    elif strSelected[-1] == "7":
        position = "c1"
    elif strSelected[-1] == "8":
        position = "c2"
    elif strSelected[-1] == "9":
        position = "c3"

    if spacefree(position):
        if turn == "X":
            selected["text"] = "X"
            insert(turn,position)
            turn = "O"
        print(selected)
    print(board)
    compMove()
    print(board)



def chfodra():
    for i in board.keys():
        if board[i] == " ":
            return False
    return True

def chfowin(player):
    if board["a1"] == board["b1"] and board["a1"] == board["c1"] and board["a1"] == player:
        return True
    elif board["a2"] == board["b2"] and board["a2"] == board["c2"] and board["a2"] == player:
        return True
    elif board["a3"] == board["b3"] and board["a3"] == board["c3"] and board["a3"] == player:
        return True
    elif board["a1"] == board["a2"] and board["a1"] == board["a3"] and board["a1"] == player:
        return True
    elif board["b1"] == board["b2"] and board["b1"] == board["b3"] and board["b1"] == player:
        return True
    elif board["c1"] == board["c2"] and board["c1"] == board["c3"] and board["c1"] == player:
        return True
    elif board["a1"] == board["b2"] and board["a1"] == board["c3"] and board["a1"] == player:
        return True
    elif board["c1"] == board["b2"] and board["c1"] == board["a3"] and board["c1"] == player:
        return True
    else:
        return False

    
def chfovapo(position):
    if position in positions:
        return True
    else:
        return False


def spacefree(position):
    if board [position] == " ":
        return True
    else:
        return False

def insert(player, position):
    global isWinner
    if chfovapo(position) == True:
        
        if spacefree(position) == True:
            board[position] = player
            if chfowin(player) == True:
                winner = Label(text=f"{player} wins")
                winner.grid(row=4,column=0,columnspan=3)
                isWinner = 1
            elif chfodra() == True:
                print("Draw")
                drawer = Label(text="draw")
                drawer.grid(row=4,column=0,columnspan=3)
        else:
            pass
    else:
        pass

p1 = "X"
p2 = "O"


title = Label(text = "Tic Tac Toe Game",bg="gray").grid(row=0,column =0,columnspan=3)
#______________________firstrow___________________________________________
a1 = Button(root,text = " ",font=("Arial",30),height = 1,width = 3)
a1.grid(row = 1,column=0)
a1.bind("<Button-1>",play)
a2 = Button(root,text = " ",font=("Arial",30),height = 1,width = 3)
a2.grid(row = 1,column=1)
a2.bind("<Button-1>",play)
a3 = Button(root,text = " ",font=("Arial",30),height = 1,width = 3)
a3.grid(row = 1,column=2)
a3.bind("<Button-1>",play)
#______________________secondrow___________________________________________
b1 = Button(root,text = " ",font=("Arial",30),height = 1,width = 3)
b1.grid(row = 2,column=0)
b1.bind("<Button-1>",play)
b2 = Button(root,text = " ",font=("Arial",30),height = 1,width = 3)
b2.grid(row = 2,column=1)
b2.bind("<Button-1>",play)
b3 = Button(root,text = " ",font=("Arial",30),height = 1,width = 3)
b3.grid(row = 2,column=2)
b3.bind("<Button-1>",play)
#______________________thirdrow___________________________________________
c1 = Button(root,text = " ",font=("Arial",30),height = 1,width = 3)
c1.grid(row = 3,column=0)
c1.bind("<Button-1>",play)
c2 = Button(root,text = " ",font=("Arial",30),height = 1,width = 3)
c2.grid(row = 3,column=1)
c2.bind("<Button-1>",play)
c3 = Button(root,text = " ",font=("Arial",30),height = 1,width = 3)
c3.grid(row = 3,column=2)
c3.bind("<Button-1>",play)

tracker = {
    "a1":a1, "a2":a2, "a3":a3,"b1":b1, "b2":b2, "b3":b3, "c1":c1, "c2":c2, "c3":c3
}

updateBoard(board)

root.mainloop()