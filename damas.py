import sys

player = 1

class Coord(object):
	"""docstring for coord"""
	def __init__(self, x = 0, y = 0):
		self.x = x 
		self.y = y
		#self.setCoord()
	def getY(self):
		return self.y
		
	def setCoord(self, x, y):
		self.x = x 
		self.y = y
		return

class Token(object):
	"""docstring for token"""
	def __init__(self, coordenada = Coord() ):
		self.coordenada = coordenada
	def eat():

		pass
	def move():
		
		pass

#ricky = Token(Coord(2,5))




x = Coord(10, 8)
y = x.getY()

class queen(Token):
	"""docstring for queen"""
	def __init__(self):
		
	def moveback():
		pass

def validation(x, y):
	cantBeUsed = False

	#if ToUication = 0:
	#	cantBeUsed = True	
	#else:
	#	cantBeUsed = False
	#return cantBeUsed
	pass



class tab(object):
	"""docstring for tab"""
	def __init__(self, arg):
		super(tab, self).__init__()
		self.arg = arg
		
movimientoValido = False

def turns():
		
	print("Player",player,"turn")

	inx = input("Enter the x coord")
	x = int(inx)
	if (x > 7) or (x < 0):
		sys.exit("Numero invalido")
	

	iny = input("Enter the y coord")
	y = int(iny)
	if (y > 7) or (y < 0):
		sys.exit("Numero invalido")
	
	print ("To")

	tox = input("Enter the x coord")
	x = int(inx)
	if (x > 7) or (x < 0):
		sys.exit("Numero invalido")
	

	toy = input("Enter the y coord")
	y = int(iny)
	if (y > 7) or (y < 0):
		sys.exit("Numero invalido")
	pass
