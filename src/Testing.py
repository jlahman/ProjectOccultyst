from Card import Card
from Board import Board
import random


deck1 = []
deckSize = 32

for i in range(32):
	deck1.append(Card()) 
	print(deck1[i])
	deck1[i].cardID = random.randint(1,512)

print(deck1)

board = Board()
board.tiles[2][4].setGamePiece(21)
board.tiles[2][5].tick()
board.draw()
