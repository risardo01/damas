import sys

#funcion pa moverse reyna
def validation():

	pass

class token(object):
	"""docstring for token"""
	def __init__(self, arg):
		super(token, self).__init__()
		self.arg = arg
	def eat():

		pass
	def movefront():

		pass

class queen(token):
	"""docstring for queen"""
	def __init__(self, arg):
		super(queen, self).__init__()
		self.arg = arg
	def moveback():
		pass


class tab(object):
	"""docstring for tab"""
	def __init__(self, arg):
		super(tab, self).__init__()
		self.arg = arg	
	#tabla
	tablero = [[0]*8 for i in range(8)]

movimientoValido = False




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
