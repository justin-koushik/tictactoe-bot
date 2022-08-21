from random import randint,choice
from os import system
class tictactoe:
	def __init__(self):
		self.player="X"
		self.bot="O"
		self.gameOver=False
		self.empty=9
		self.board=[[" " for i in range(3)] for j in range(3)]
	def reset(self):
		self.player="X"
		self.bot="O"
		player2=int(input("do u wanna play against bot? 1-yes 0-no "))
		if player2:
			self.getstatefun=self.Bot
		else:
			self.getstatefun=self.human
		self.gameOver=False
		self.empty=9
		self.board=[[" " for i in range(3)] for j in range(3)]
		choice=int(input("do u want O ? 1-yes 0-no "))
		if choice:
			self.player,self.bot=self.bot,self.player
		#print(f"you - {self.player} player2 - {self.bot}")
		self.turn = randint(0,1)
	def draw(self):
		system("cls")
		print(f"you - {self.player} player2 - {self.bot}")
		print("\n")
		print(" ",end=" ")
		for i in range(3):
			print(i,end="    ")
		print("\n")
		for k in range(3):
			print(k,end="  ")
			for i in range(3):
				print(self.board[k][i],end=" ")
				if i<2:
					print("|",end=" ")
			print("\n")
			if k<2:
				print("  ",end=" ")
				for i in range(3):
					print("_",end="   ")
				print("\n")
	def setState(self,i,j):
		self.board[i][j]=f"{self.player}" if self.turn else f"{self.bot}"
		self.empty-=1
		self.check(i,j)
	def check(self,i,j):
		if self.board[i][0]==self.board[i][1]==self.board[i][2]:
			self.gameOver=True
			return
		if self.board[0][j]==self.board[1][j]==self.board[2][j]:
			self.gameOver=True
			return
		if not (i+j)&1:
			if i==j:
				if self.board[0][0]==self.board[1][1]==self.board[2][2]:
					self.gameOver=True
					return
				if i==1:
					if self.board[0][2]==self.board[1][1]==self.board[2][0]:
						self.gameOver=True
						return
			else:
				if self.board[0][2]==self.board[1][1]==self.board[2][0]:
					self.gameOver=True
					return
	def compare(self,score,bestscore):
		if self.turn:
			return score>bestscore
		return score<bestscore
	def Bot(self,depth=0):
		if self.gameOver:
			if self.turn:
				return 1
			return -1
		else:
			if not self.empty:
				return 0
		bestscore=(-1)**(self.turn+1)*2
		bestmoves=[]
		for i in range(3):
			for j in range(3):
				if self.board[i][j]==" ":
					self.setState(i,j)
					self.turn=not self.turn
					score=self.Bot(depth+1)
					if self.compare(score,bestscore):
						bestscore=score
						if not depth:
							bestmoves=[[i,j]]
					elif not depth:
						if score==bestscore:
							bestmoves.append([i,j])
					self.board[i][j]=" "
					self.empty+=1
					self.gameOver=False
					self.turn=not self.turn
		if depth:
			return bestscore
		else:
			bestmove=choice(bestmoves)
			self.setState(*bestmove)
	def getInput(self):
		pos=input("enter pos [rc] :")
		i=int(pos[0])
		j=int(pos[1])
		if i>2 or i<0 or j>2 or j<0:
			print("try values between 0 - 2")
			return self.getInput()
		else:
			return i,j
	def human(self):
		i,j = self.getInput()
		if self.board[i][j]!=" ":
			print(f"already filled with {self.board[i][j]}")
			self.human()
		else:
			self.setState(i,j)
	def play(self):
		self.reset()
		self.draw()
		while (not self.gameOver) and self.empty:	
				if self.turn:
					print(f"{self.player} turn")
					self.human()
				else:
					print(f"{self.bot} turn")
					self.getstatefun()
				self.draw()
				if not self.gameOver:
					self.turn=not self.turn
		if self.gameOver:
			winner=f"{self.player}" if self.turn else f"{self.bot}"
			print(f" winner is {winner} ☆")
		else:
			print("Draw!!")
		play=int(input("do u wanna play again? 1 -yes 0 -no "))
		if play:
			self.play()
	def __setitem__(self,key,val):
		x,y=key
		if self.board[x][y]==" ":
			self.board[x][y]=val
			self.empty-=1
		else:
			raise KeyError("given key is not empty")
	def __getitem__(self,key):
		x,y=key
		return self.board[x][y]
	def __delitem__(self,key):
		x,y=key
		if not self.board[x][y]==" ":
			self.board[x][y]=" "
			self.empty+=1
	def __repr__(self):
		self.draw()
		return ""
a=tictactoe()
#a.bot="X"
#a.player="O"
#a[1,1]="X"
#a[2,0]="O"
#a[2,2]="O"
#a[1,0]="X"
#print(a.empty,a)
#del a[1,0]
#print(a.empty,a)
#a.turn=0
#a.Bot()
a.play()