import sys

player = 1


<<<<<<< HEAD
class Token(object):
=======
class Coken(object):
>>>>>>> 6de733357135090abd559537bd66b309bbff47c0
	"""docstring for token"""
	def __init__(self, coordenada = Coord() ):
		self.coordenada = coordenada
	def eat():

		pass
	def move():
		
		pass

<<<<<<< HEAD

ricky = Token(Coord(2,5))


=======
>>>>>>> 6de733357135090abd559537bd66b309bbff47c0
class Coord(object):
	"""docstring for coord"""
	def __init__(self, x = 0, y = 0):
		self.x = x 
<<<<<<< HEAD
		self.y = y
		#self.setCoord()
	def getY(self):
		return self.y
		
	def setCoord(self, x, y):
		self.x = x 
		self.y = y
		return

x = Coord(10, 8)
y = x.getY()
=======
		self.y = y 
	def getCoords(self):
		
		return (self.x, self.y)
		pass
	def setCoord(self, x, y):
		
		pass
>>>>>>> 6de733357135090abd559537bd66b309bbff47c0

class queen(token):
	"""docstring for queen"""
	def __init__(self, arg):
		super(queen, self).__init__()
		self.arg = arg
	def moveback():
		pass

<<<<<<< HEAD
def validation(x, y):
=======
def validation(ubic):
>>>>>>> 6de733357135090abd559537bd66b309bbff47c0
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
	#tabla
	tablero0 = [[0]for i in range(8)]
	tablero1 = [[0]for i in range(8)]
	tablero2 = [[0]for i in range(8)]
	tablero3 = [[0]for i in range(8)]
	tablero4 = [[0]for i in range(8)]
	tablero5 = [[0]for i in range(8)]
	tablero6 = [[0]for i in range(8)]
	tablero7 = [[0]for i in range(8)]

	tablero0y = [[0]for i in range(8)]
	tablero1y = [[0]for i in range(8)]
	tablero2y = [[0]for i in range(8)]
	tablero3y = [[0]for i in range(8)]
	tablero4y = [[0]for i in range(8)]
	tablero5y = [[0]for i in range(8)]
	tablero6y = [[0]for i in range(8)]
	tablero7y = [[0]for i in range(8)]

	tablero0[1] = '1'
	tablero0[3] = '1'
	tablero0[5] = '1'
	tablero0[7] = '1'

	tablero1[0] = '1'
	tablero1[2] = '1'
	tablero1[4] = '1'
	tablero1[6] = '1'

	tablero2[1] = '1'
	tablero2[3] = '1'
	tablero2[5] = '1'
	tablero2[7] = '1'

	tablero3[0] = '1'
	tablero3[2] = '1'
	tablero3[4] = '1'
	tablero3[6] = '1'

	tablero4[1] = '1'
	tablero4[3] = '1'
	tablero4[5] = '1'
	tablero4[7] = '1'

	tablero5[0] = '1'
	tablero5[2] = '1'
	tablero5[4] = '1'
	tablero5[6] = '1'

	tablero6[1] = '1'
	tablero6[3] = '1'
	tablero6[5] = '1'
	tablero6[7] = '1'

	tablero7[0] = '1'
	tablero7[2] = '1'
	tablero7[4] = '1'
	tablero7[6] = '1'
	#◻ ■ ⬤
	#tablero

	tablero0[0] = '⬤'
	tablero0[2] = '⬤'
	tablero0[4] = '⬤'
	tablero0[6] = '⬤'

	tablero1[1] = '⬤'
	tablero1[3] = '⬤'
	tablero1[5] = '⬤'
	tablero1[7] = '⬤'



	tablero6[0] = '⬤'
	tablero6[2] = '⬤'
	tablero6[4] = '⬤'
	tablero6[6] = '⬤'

	tablero7[1] = '⬤'
	tablero7[3] = '⬤'
	tablero7[5] = '⬤'
	tablero7[7] = '⬤'


	#lado y
	tablero0y[0] = tablero0[0]
	tablero0y[6] = tablero6[0]

	tablero1y[1] = tablero1[1]
	tablero1y[7] = tablero7[1]

	tablero2y[0] = tablero0[2]
	tablero2y[6] = tablero6[2]

	tablero3y[1] = tablero1[3]
	tablero3y[7] = tablero7[3]

	tablero4y[0] = tablero0[4]
	tablero4y[6] = tablero6[4]

	tablero5y[1] = tablero1[5]
	tablero5y[7] = tablero7[5]

	tablero6y[0] = tablero0[6]
	tablero6y[6] = tablero6[6]

	tablero7y[1] = tablero1[7]
	tablero7y[7] = tablero7[7]

	
	print (tablero7)
	print (tablero6)
	print (tablero5)
	print (tablero4)
	print (tablero3)
	print (tablero2)
	print (tablero1)
	print (tablero0)
<<<<<<< HEAD
=======

>>>>>>> 6de733357135090abd559537bd66b309bbff47c0




		
movimientoValido = False


<<<<<<< HEAD
		
movimientoValido = False


=======
>>>>>>> 6de733357135090abd559537bd66b309bbff47c0
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
