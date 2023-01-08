
from tkinter import *
from tkinter import messagebox
import random
def positionIsFree(position):
	if(position >= 1 and position <=9 and table[position-1]==" "):
		return True
	else:
		return False
def insertInPosition(letter, position):
	if positionIsFree(position):
		table[position-1] = letter
		dob(letter,position)
		if checkDraw():
			messagebox.showerror(" tic iac toe","DRAWW")
		if checkPossibleWins():
			if letter == 'X':
				messagebox.showerror(" tic iac toe","COMPUTER WON")
			else:
				messagebox.showerror(" tic iac toe","YOU WON")
	else:
		messagebox.showerror(" tic iac toe","pick another one")	
def checkPossibleWins():
	win=False
	if (table[0] == table[1] == table[2] and table[0]!= " "):
		win=True
	elif(table[3] == table[4] == table[5] and table[3]!= " "):
		win=True
	elif(table[6] == table[7] == table[8] and table[6]!= " "):
		win=True
	elif(table[0] == table[3] == table[6] and table[0]!= " "):
		win=True
	elif(table[1] == table[4] == table[7] and table[1]!= " "):
		win=True
	elif(table[2] == table[5] == table[8] and table[2]!= " "):
		win=True
	elif(table[0] == table[4] == table[8] and table[0]!= " "):
		win=True
	elif(table[2] == table[4] == table[6] and table[2]!= " "):
		win=True
	return win
def checkWhichMarkWon(mark):
	winner=""
	if (table[0] == table[1] == table[2] and table[0]!= " "):
		winner=table[0]
	elif(table[3] == table[4] == table[5] and table[3]!= " "):
		winner=table[3]
	elif(table[6] == table[7] == table[8] and table[6]!= " "):
		winner=table[6]
	elif(table[0] == table[3] == table[6] and table[0]!= " "):
		winner=table[0]
	elif(table[1] == table[4] == table[7] and table[1]!= " "):
		winner=table[1]
	elif(table[2] == table[5] == table[8] and table[2]!= " "):
		winner=table[2]
	elif(table[0] == table[4] == table[8] and table[0]!= " "):
		winner=table[0]
	elif(table[2] == table[4] == table[6] and table[2]!= " "):
		winner=table[2]
	if winner == mark :
			return True
	else:
			return False
def checkDraw():
	if(checkPossibleWins() == False and table.count(" ") == 0):
		return True
	else :
		return False	
def computerMove():
	HigherScore= -2
	position=0
	for i in range(len(table)):
		if (table[i] == " "):
			table[i] = computer
			score = MiniMAX(table,False)
			table[i] = " "
			if(score > HigherScore):
				HigherScore = score
				position = i+1
	insertInPosition(computer, position)
def MiniMAX(table, isMaximizing):
	if checkWhichMarkWon(computer):   
		return 1
	elif checkWhichMarkWon(player):
		return -1
	elif checkDraw():
		return 0
	if (isMaximizing):
		HighestScore = -2
		for i in range(len(table)):
			if (table[i] == " "):
				table[i] = computer
				score = MiniMAX(table, False)
				table[i] = " "
				if (score > HighestScore):
					HighestScore = score
		return HighestScore
	else:
		HighestScore = 10
		for i in range(len(table)):
			if (table[i] == " "):
				table[i] = player
				score = MiniMAX(table, True)
				table[i] = " "
				if (score < HighestScore):
					HighestScore = score
		return HighestScore
def positionstobuttonss(position):
	if (position==1):
		b=b1
	elif(position==2):
		b=b2
	elif(position==3):
		b=b3	
	elif(position==4):
		b=b4
	elif(position==5):
		b=b5
	elif(position==6):
		b=b6
	elif(position==7):
		b=b7
	elif(position==8):
		b=b8
	elif(position==9):
		b=b9	
	return b 
def buttonstopositions(b):
	if (b==b1):
		position=1
	elif(b==b2):
		position=2
	elif(b==b3):
		position=3	
	elif(b==b4):
		position=4
	elif(b==b5):
		position=5
	elif(b==b6):
		position=6
	elif(b==b7):
		position=7
	elif(b==b8):
		position=8
	elif(b==b9):
		position=9
	return position
def dob(letter,position):
	b=positionstobuttonss(position)
	b.configure(text=letter,font=("Times", "10", "bold"), bg='white', fg='blue')
	table[position-1]=letter
def b_click(b):
	position=buttonstopositions(b)
	insertInPosition(player,position)
	computerMove()	
def randommove():
	list1 = [1, 2, 3, 4, 5, 6,7,8,9]
	pos=random.choice(list1)
	insertInPosition("X",pos)
def NewGame():
	for i in range (9):
		table[i]=" "
		buttonn=positionstobuttonss(i+1)
		buttonn.configure(text=" ",font=("Times", "10", "bold"), bg='blue', fg='black')
	randommove()
table = [" " for x in range(9)]
player = 'O'
computer = 'X'
wind = Tk()
wind.configure(background="grey")
wind.title("GROUP-10 << Tic Tac Toe >>")
Label(wind, text="Group-10-Project", font=('Ariel', 12))
wind.geometry("240x345")

b1 = Button(wind, text=' ',font=("Times", "10", "bold"), fg='black', bg='blue', command=lambda: b_click(b1), height=5, width=10)
b1.grid(row=1, column=0)

b2 = Button(wind, text=' ',font=("Times", "10", "bold"), fg='black', bg='blue', command=lambda: b_click(b2), height=5, width=10)
b2.grid(row=1, column=1)

b3 = Button(wind, text=' ',font=("Times", "10", "bold"), fg='black', bg='blue', command=lambda: b_click(b3), height=5, width=10)
b3.grid(row=1, column=2)

b4 = Button(wind, text=' ',font=("Times", "10", "bold"), fg='black', bg='blue', command=lambda: b_click(b4), height=5, width=10)
b4.grid(row=2, column=0)

b5 = Button(wind, text=' ',font=("Times", "10", "bold"), fg='black', bg='blue', command=lambda: b_click(b5), height=5, width=10)
b5.grid(row=2, column=1)

b6 = Button(wind, text=' ',font=("Times", "10", "bold"), fg='black', bg='blue', command=lambda: b_click(b6), height=5, width=10)
b6.grid(row=2, column=2)

b7 = Button(wind, text=' ',font=("Times", "10", "bold"), fg='black', bg='blue', command=lambda: b_click(b7), height=5, width=10)
b7.grid(row=3, column=0)

b8 = Button(wind, text=' ',font=("Times", "10", "bold"), fg='black', bg='blue', command=lambda: b_click(b8), height=5, width=10)
b8.grid(row=3, column=1)

b9 = Button(wind, text=' ',font=("Times", "10", "bold"), fg='black', bg='blue', command=lambda: b_click(b9), height=5, width=10)
b9.grid(row=3, column=2)

restartbutton=Button(wind, text='Restart',font=("Times", "10", "bold"),fg='blue', bg='white', command=NewGame, height=5, width=35)
restartbutton.grid(row=0, columnspan=100)
randommove()
wind.mainloop()
