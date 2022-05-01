from ast import arg
from tkinter import *
import tkinter.messagebox

root = Tk()

#Window settings

root.geometry("1350x750+0+0")
root.title("Tic Tac Toe Game | Made by Oxydis")
root.config(background='#2b2b2b')

Tops = Frame(root, bg='#2b2b2b', pady=2, width=1350, height=100, relief=RIDGE)
Tops.grid(row=0, column=0)

lblTtile = Label(Tops, font=('arial',50,'bold'), text="Tic Tac Toe Game", bd=21, bg='#2b2b2b', fg="Cornsilk", justify="center")
lblTtile.grid(row=0, column=0)

MainFrame = Frame(root, bg='black', pady=2, width=1350, height=100, relief=RIDGE)
MainFrame.grid(row=1, column=0)

#Frames position

LeftFrame = Frame(MainFrame, bd=10, width=750, height=500, pady=2, padx=10, bg="#2b2b2b", relief=RIDGE)
LeftFrame.pack(side=LEFT)

RightFrame = Frame(MainFrame, bd=10, width=560, height=500, padx=10, pady=2, bg='#2b2b2b', relief=RIDGE)
RightFrame.pack(side=RIGHT)

RightFrame1 = Frame(RightFrame, bd=10, width=560, height=200, padx=10, pady=2, bg='#2b2b2b', relief=RIDGE)
RightFrame1.grid(row=0, column=0)

RightFrame2 = Frame(RightFrame, bd=10, width=560, height=200, padx=10, pady=2, bg='#2b2b2b', relief=RIDGE)
RightFrame2.grid(row=1, column=0)


PlayerX = IntVar()
PlayerO = IntVar()
MancheA = IntVar()

PlayerX.set(0)
PlayerO.set(0)
MancheA.set(1)

button = StringVar()
click = True

def checker(buttons):
    global click
    if buttons["text"] == " " and click == True:
        buttons["text"] = "X"
        click = False
        scorekeeper()
    elif buttons["text"] == " " and click == False:
        buttons["text"] = "O"
        click = True
        scorekeeper()

def reset():
    button1["text"] = " "
    button2["text"] = " "
    button3["text"] = " "
    button4["text"] = " "
    button5["text"] = " "
    button6["text"] = " "
    button7["text"] = " "
    button8["text"] = " "
    button9["text"] = " "

    button1.configure(background='gainsboro')
    button2.configure(background='gainsboro')
    button3.configure(background='gainsboro')
    button4.configure(background='gainsboro')
    button5.configure(background='gainsboro')
    button6.configure(background='gainsboro')
    button7.configure(background='gainsboro')
    button8.configure(background='gainsboro')
    button9.configure(background='gainsboro')

def newgame():
    reset()
    PlayerX.set(0)
    PlayerO.set(0)
    MancheA.set(0)

def scorekeeper():
    #Joueur de X
    #verticale
    if(button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X"):
        button1.configure(background='#2b2b2b')
        button2.configure(background='#2b2b2b')
        button3.configure(background='#2b2b2b')
        n = float(PlayerX.get())
        score = n + 1
        PlayerX.set(score)
        i = float(MancheA.get())
        all = i + 1
        MancheA.set(all)
        tkinter.messagebox.showinfo("Victoire d'un joueur", "Le joueur X a gagné 1 point")
    
    if(button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X"):
        button4.configure(background='#2b2b2b')
        button5.configure(background='#2b2b2b')
        button6.configure(background='#2b2b2b')
        n = float(PlayerX.get())
        score = n + 1
        PlayerX.set(score)
        i = float(MancheA.get())
        all = i + 1
        MancheA.set(all)
        tkinter.messagebox.showinfo("Victoire d'un joueur", "Le joueur X a gagné 1 point")

    if(button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X"):
        button7.configure(background='#2b2b2b')
        button8.configure(background='#2b2b2b')
        button9.configure(background='#2b2b2b')
        n = float(PlayerX.get())
        score = n + 1
        PlayerX.set(score)
        i = float(MancheA.get())
        all = i + 1
        MancheA.set(all)
        tkinter.messagebox.showinfo("Victoire d'un joueur", "Le joueur X a gagné 1 point")
    #horizontale
    if(button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X"):
        button1.configure(background='#2b2b2b')
        button4.configure(background='#2b2b2b')
        button7.configure(background='#2b2b2b')
        n = float(PlayerX.get())
        score = n + 1
        PlayerX.set(score)
        i = float(MancheA.get())
        all = i + 1
        MancheA.set(all)
        tkinter.messagebox.showinfo("Victoire d'un joueur", "Le joueur X a gagné 1 point")

    if(button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X"):
        button2.configure(background='#2b2b2b')
        button5.configure(background='#2b2b2b')
        button8.configure(background='#2b2b2b')
        n = float(PlayerX.get())
        score = n + 1
        PlayerX.set(score)
        i = float(MancheA.get())
        all = i + 1
        MancheA.set(all)
        tkinter.messagebox.showinfo("Victoire d'un joueur", "Le joueur X a gagné 1 point")

    if(button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X"):
        button3.configure(background='#2b2b2b')
        button6.configure(background='#2b2b2b')
        button9.configure(background='#2b2b2b')
        n = float(PlayerX.get())
        score = n + 1
        PlayerX.set(score)
        i = float(MancheA.get())
        all = i + 1
        MancheA.set(all)
        tkinter.messagebox.showinfo("Victoire d'un joueur", "Le joueur X a gagné 1 point")
    #diagonales
    if(button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X"):
        button1.configure(background='#2b2b2b')
        button5.configure(background='#2b2b2b')
        button9.configure(background='#2b2b2b')
        n = float(PlayerX.get())
        score = n + 1
        PlayerX.set(score)
        i = float(MancheA.get())
        all = i + 1
        MancheA.set(all)
        tkinter.messagebox.showinfo("Victoire d'un joueur", "Le joueur X a gagné 1 point")

    if(button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X"):
        button3.configure(background='#2b2b2b')
        button5.configure(background='#2b2b2b')
        button7.configure(background='#2b2b2b')
        n = float(PlayerX.get())
        score = n + 1
        PlayerX.set(score)
        i = float(MancheA.get())
        all = i + 1
        MancheA.set(all)
        tkinter.messagebox.showinfo("Victoire d'un joueur", "Le joueur X a gagné 1 point")
    
    #Joueur de O
    #verticale
    if(button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O"):
        button1.configure(background='#2b2b2b')
        button2.configure(background='#2b2b2b')
        button3.configure(background='#2b2b2b')
        n = float(PlayerO.get())
        score = n + 1
        PlayerO.set(score)
        i = float(MancheA.get())
        all = i + 1
        MancheA.set(all)
        tkinter.messagebox.showinfo("Victoire d'un joueur", "Le joueur O a gagné 1 point")
    
    if(button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O"):
        button4.configure(background='#2b2b2b')
        button5.configure(background='#2b2b2b')
        button6.configure(background='#2b2b2b')
        n = float(PlayerO.get())
        score = n + 1
        PlayerO.set(score)
        i = float(MancheA.get())
        all = i + 1
        MancheA.set(all)
        tkinter.messagebox.showinfo("Victoire d'un joueur", "Le joueur O a gagné 1 point")

    if(button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O"):
        button7.configure(background='#2b2b2b')
        button8.configure(background='#2b2b2b')
        button9.configure(background='#2b2b2b')
        n = float(PlayerO.get())
        score = n + 1
        PlayerO.set(score)
        i = float(MancheA.get())
        all = i + 1
        MancheA.set(all)
        tkinter.messagebox.showinfo("Victoire d'un joueur", "Le joueur O a gagné 1 point")
    #horizontale
    if(button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O"):
        button1.configure(background='#2b2b2b')
        button4.configure(background='#2b2b2b')
        button7.configure(background='#2b2b2b')
        n = float(PlayerO.get())
        score = n + 1
        PlayerO.set(score)
        i = float(MancheA.get())
        all = i + 1
        MancheA.set(all)
        tkinter.messagebox.showinfo("Victoire d'un joueur", "Le joueur O a gagné 1 point")

    if(button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O"):
        button2.configure(background='#2b2b2b')
        button5.configure(background='#2b2b2b')
        button8.configure(background='#2b2b2b')
        n = float(PlayerO.get())
        score = n + 1
        PlayerO.set(score)
        i = float(MancheA.get())
        all = i + 1
        MancheA.set(all)
        tkinter.messagebox.showinfo("Victoire d'un joueur", "Le joueur O a gagné 1 point")

    if(button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O"):
        button3.configure(background='#2b2b2b')
        button6.configure(background='#2b2b2b')
        button9.configure(background='#2b2b2b')
        n = float(PlayerO.get())
        score = n + 1
        PlayerO.set(score)
        i = float(MancheA.get())
        all = i + 1
        MancheA.set(all)
        tkinter.messagebox.showinfo("Victoire d'un joueur", "Le joueur O a gagné 1 point")
    #diagonales
    if(button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O"):
        button1.configure(background='#2b2b2b')
        button5.configure(background='#2b2b2b')
        button9.configure(background='#2b2b2b')
        n = float(PlayerO.get())
        score = n + 1
        PlayerO.set(score)
        i = float(MancheA.get())
        all = i + 1
        MancheA.set(all)
        tkinter.messagebox.showinfo("Victoire d'un joueur", "Le joueur O a gagné 1 point")

    if(button3["text"] == "O" and button5["text"] == "O" and button7["text"] == "O"):
        button3.configure(background='#2b2b2b')
        button5.configure(background='#2b2b2b')
        button7.configure(background='#2b2b2b')
        n = float(PlayerO.get())
        score = n + 1
        PlayerO.set(score)
        i = float(MancheA.get())
        all = i + 1
        MancheA.set(all)
        tkinter.messagebox.showinfo("Victoire d'un joueur", "Le joueur O a gagné 1 point")

    if(score == 10):
        newgame()
        tkinter.messagebox.showinfo("Partie est terminée", "La partie c'est terminé car un joueur à atteint 10 points")


lblPlayerX = Label(RightFrame1, font=('arial', 40, 'bold'), text="Player X :", padx=2, pady=2, bg="#2b2b2b")
lblPlayerX.grid(row=0, column=0, sticky=W)
txtPlayerX = Entry(RightFrame1, font=('arial', 40, 'bold'), bd=2, bg='#2b2b2b', fg='black', textvariable=PlayerX, width=14, justify=LEFT)
txtPlayerX.grid(row=0, column=1)

lblPlayerO = Label(RightFrame1, font=('arial', 40, 'bold'), text="Player O :", padx=2, pady=2, bg="#2b2b2b")
lblPlayerO.grid(row=1, column=0, sticky=W)
txtPlayerO = Entry(RightFrame1, font=('arial', 40, 'bold'), bd=2, bg='#2b2b2b', fg='black', textvariable=PlayerO, width=14, justify=LEFT)
txtPlayerO.grid(row=1, column=1)

btnReset = Button(RightFrame2, text="Reset", font=('Times 40 bold'), width=20, height=1, bg='gainsboro', command=lambda:reset())
btnReset.grid(row=2, column=0, padx=6, pady=11)


lblsbTtile = Label(Tops, font=('arial',20,'bold'), text="Manche :", bd=21, bg='#2b2b2b', fg="Cornsilk", justify=CENTER)
lblsbTtile.grid(row=1, column=0)
txtMancheA = Entry(Tops, font=('arial', 20, 'bold'), bd=2, bg='#2b2b2b', fg='black', textvariable=MancheA, width=14, justify=CENTER)
txtMancheA.grid(row=1, column=1)

btnGame = Button(RightFrame2, text="New Game", font=('Times 40 bold'), width=20, height=1, bg='gainsboro', command=lambda:newgame())
btnGame.grid(row=3, column=0, padx=6, pady=11)

button1 = Button(LeftFrame, text=" ", font=('arial 26 bold'), width=8, height=3, bg='gainsboro', command=lambda:checker(button1))
button1.grid(row=1, column=0, sticky=S+N+E+W)

button2 = Button(LeftFrame, text=" ", font=('arial 26 bold'), width=8, height=3, bg='gainsboro', command=lambda:checker(button2))
button2.grid(row=1, column=1, sticky=S+N+E+W)

button3 = Button(LeftFrame, text=" ", font=('arial 26 bold'), width=8, height=3, bg='gainsboro', command=lambda:checker(button3))
button3.grid(row=1, column=2, sticky=S+N+E+W)

button4 = Button(LeftFrame, text=" ", font=('arial 26 bold'), width=8, height=3, bg='gainsboro', command=lambda:checker(button4))
button4.grid(row=2, column=0, sticky=S+N+E+W)

button5 = Button(LeftFrame, text=" ", font=('arial 26 bold'), width=8, height=3, bg='gainsboro', command=lambda:checker(button5))
button5.grid(row=2, column=1, sticky=S+N+E+W)

button6 = Button(LeftFrame, text=" ", font=('arial 26 bold'), width=8, height=3, bg='gainsboro', command=lambda:checker(button6))
button6.grid(row=2, column=2, sticky=S+N+E+W)

button7 = Button(LeftFrame, text=" ", font=('arial 26 bold'), width=8, height=3, bg='gainsboro', command=lambda:checker(button7))
button7.grid(row=3, column=0, sticky=S+N+E+W)

button8 = Button(LeftFrame, text=" ", font=('arial 26 bold'), width=8, height=3, bg='gainsboro', command=lambda:checker(button8))
button8.grid(row=3, column=1, sticky=S+N+E+W)

button9 = Button(LeftFrame, text=" ", font=('arial 26 bold'), width=8, height=3, bg='gainsboro', command=lambda:checker(button9))
button9.grid(row=3, column=2, sticky=S+N+E+W)


root.mainloop()