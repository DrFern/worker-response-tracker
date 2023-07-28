class Game:
	def __init__(self):
		self.board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]

		# instructions
		self.instructions_board = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
		print("You can go by pressing 1 throush 9")
		for row in self.instructions_board:
			for item in row:
				print(item, end=" ")
			print()

		print()
		print()

	def move(self, player):
		if player == 1:
			marker = "X"
			move = input("Where would you like to move?	")
			if move == 1:
				self.board[0][0] = marker
			elif move == 2:
				self.board[0][1] = marker
			elif move == 3:
				self.board[0][2] = marker
			elif move == 4:
				self.board[1][0] = marker
			elif move == 5:
				self.board[1][1] = marker
			elif move == 6:
				self.board[1][2] = marker
			elif move == 7:
				self.board[2][0] = marker
			elif move == 8:
				self.board[2][1] = marker
			elif move == 9:
				self.board[2][2] = marker
		else:
			marker = "O"
			pass

	def display(self):
		for row in self.board:
			for item in row:
				print(item, end=" ")
			print()



game = Game()
game.display()
game.move(1)
game.display()