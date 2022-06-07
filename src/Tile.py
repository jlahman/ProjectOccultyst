class Tile:
	isOccupied = False
	occupyingPiece = None

	def setGamePiece(self, Piece):
		self.occupyingPiece = Piece
		self.isOccupied = True
		pass

	def tick(self):
		pass

	
	
class ManaTile(Tile):
	def tick(self):
		if(self.isOccupied):
			print("Add Mana to Player on piece")