import sys

player = 1

validLetters = 'ABCDEFGH'

class Coord(object):
	"""docstring for coord"""
	def __init__(self, x = 0, y = 0):
		self.x = x 
		self.y = y
		#self.setCoord()
	def getY(self):
		return self.y
	def getX(self):
		return self.x
	def setCoord(self, coord):
		self.x = coord.getX()
		self.y = coord.getY()
	def __add__(self, coord):
		self.x = self.x + coord.getX()
		self.y = self.y + coord.getY()

class Player (object):
	def __init__(self, num):
		self.num = num
	def getNumPlayer(self):
		return self.num
	def setNumPlayer(self, num):
		self.num = num


#cor1+cor2

class Token(object):
	"""docstring for token"""
	def __init__(self, coordenada = Coord(), color = True):
		self.coordenada = coordenada
		self.color = color #True = White --- False = Red
	#def eat(self):
		
	def move(self, coordenada):
		self.coordenada.setCoord(coordenada)
		
#ricky = Token(Coord(2,5))

class Board(object):
	"""docstring for tab"""
	def __init__(self):
		self.red_token = []
		self.white_token = []
		
		self.red_token.append( Token(Coord(0, 0), False) ) #1
		self.red_token.append( Token(Coord(2, 0), False) ) #2
		self.red_token.append( Token(Coord(4, 0), False) ) #3 
		self.red_token.append( Token(Coord(6, 0), False) ) #4
		self.red_token.append( Token(Coord(1, 1), False) ) #5
		self.red_token.append( Token(Coord(3, 1), False) ) #6
		self.red_token.append( Token(Coord(5, 1), False) ) #7
		self.red_token.append( Token(Coord(7, 1), False) ) #8

		self.white_token.append( Token(Coord(0, 7), True) ) #1
		self.white_token.append( Token(Coord(2, 7), True) ) #2
		self.white_token.append( Token(Coord(4, 7), True) ) #3 
		self.white_token.append( Token(Coord(6, 7), True) ) #4
		self.white_token.append( Token(Coord(1, 6), True) ) #5
		self.white_token.append( Token(Coord(3, 6), True) ) #6
		self.white_token.append( Token(Coord(5, 6), True) ) #7
		self.white_token.append( Token(Coord(7, 6), True) ) #8

	def __str__(self):
		s = "   A B C D E F G H\n\n"
		for y in range(0,8):
			s+=str(y)+"  "
			for x in range(0,8):
				
				s+="- "#
				for i in range(0,8):
					if (x == self.red_token[i].coordenada.getX()) and (y == self.red_token[i].coordenada.getY()):
						s = s[:-2] #Rm last char
						s+="\033[31m" + "0 " + "\033[0m"
						break
					elif (x == self.white_token[i].coordenada.getX()) and (y == self.white_token[i].coordenada.getY()):
						s = s[:-2] #Rm last char
						s+="\033[34m" + "0 " + "\033[0m"
						break
					
				
			s+="\n"	
		return s

#dic = Board()
#print(dic)
'''
class queen(Token):
	"""docstring for queen"""
	def __init__(self):
		
	#def moveback():
		

def validation():
	cantBeUsed = False

	#if ToUication = 0:
	#	cantBeUsed = True	
	#else:
	#	cantBeUsed = False
	#return cantBeUsed


class validation(object):
	def __init__(self, letter, number)
		self.letter = letter
		self.number = number

	def letter(self, letter)


	def number(self, number)
'''
	

def Turns(player):
		
	print("Player",player,"turn")

	coord = input("Enter the token coord (example: A:2)")
	litArray = coord.split(":")
	x = int(litArray[1])
	if (x > 7) or (x < 0):
		sys.exit("Numero invalido")
	
	#print(litArray[1])
	
	
	coord = input("Enter the coord to go (example: A:2)")
	litArray = coord.split(":")

	#validation.letter(litArray[0])
	#validation.number(litArray[1])

	x = int(litArray[1])
	if (x > 7) or (x < 0):
		sys.exit("Numero invalido")
	

	'''
	tox = input("Enter the x coord")
	x = int(inx)
	if (x > 7) or (x < 0):
		sys.exit("Numero invalido")
	

	toy = input("Enter the y coord")
	y = int(iny)
	if (y > 7) or (y < 0):
		sys.exit("Numero invalido")'''

dic = Turns(1)
print(dic)
