from random import randint

class Entity:
	def __init__(self, x, y, graphic, hp, cur_hp, damage):
		self.x = x
		self.y = y
		self.graphic = graphic
		self.direction = direction

	def Player(Entity):
		def __init__(self, x, y, graphic, hp, cur_hp, damage):
			Entity.__init__(self, x, y, graphic, hp, cur_hp, damage)
			self.hp = hp
			self.cur_hp = cur_hp
		
		def Position(self, x, y):
			return Player.Position(x, y)
	
		def Move(self, x, y):
			D = input("")
			if D == "n":
				return Player.Move(x, y+1)
			elif D == "s":
				return Player.Move(x, y-1)
			elif D == "w":
				return Player.Move(x-1, y)
			elif D == "e":
				return Player.Move(x+1, y)
	
	def Monster(Entity):
		def __init__(self, x, y, graphic, hp, cur_hp, damage):
			Entity.__init__(self, x, y, graphic, hp, cur_hp, damage)
			
	
		def Position(self, x, y):
			return Monster.Position(x, y)

		def Move(self, direction, damage):
			d = random.randint(1, 4)
			if d == 1:
				return Monster.Move(x, y+1)
			elif d == 2:
				return Monster.Move(x, y-1)
			elif d == 3:
				return Monster.Move(x-1, y)
			elif d == 4:
				return Monster.Move(x+1, y)




#-------------------------------------------------------------------
#___________________________________________________________________
