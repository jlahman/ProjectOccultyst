from Tile import Tile, ManaTile

class Board:
	COLS = 9
	ROWS = 5
	
	def __init__(self):
		self.tiles = [[Tile() for i in range(self.COLS)] for j in range(self.ROWS)]
		self.tiles[2][5] = ManaTile()
		self.tiles[1][4] = ManaTile()
		self.tiles[3][4] = ManaTile()


	def draw(self):
		VERT_SEP = "|"
		HORI_SEP = "-"
		canvas = ""
		for r in range(self.ROWS):
			for c in range(self.COLS):
				if(self.tiles[r][c].occupyingPiece == None):
					spaceMarker = "__"
					if(type(self.tiles[r][c]) is ManaTile):
						spaceMarker = "{}"
					if(c == self.COLS - 1):
						canvas += spaceMarker
					else:
						canvas += spaceMarker + VERT_SEP
				elif(self.tiles[r][c].occupyingPiece != None):
					canvas += str(self.tiles[r][c].occupyingPiece) + VERT_SEP
			canvas += "\n"

		print(canvas)



