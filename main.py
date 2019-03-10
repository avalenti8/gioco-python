from random import randint

class Entity:
	def __init__(self, x, y, graphic):
		self.x = x
		self.y = y
		self.graphic = graphic
		self.direction = direction

	class Player(Entity):
		def __init__(self, x, y, graphic):
			Entity.__init__(self, x, y, graphic, hp, cur_hp, damage)
			self.hp = hp
			self.cur_hp = cur_hp
	
	class Monster(Entity):
		def __init__(self, x, y, graphic):
			Entity.__init__(self, x, y, graphic, hp, cur_hp, damage)

class Level:
	def __init__(self, w, h):
    	self.w = w
    	self.h = h
    	self.entities = []

  	def draw(self):
    	for y in range(self.h):
      		for x in range(self.w):
       			for e in self.entities:
          			if e.x == x and e.y == y:
           				print("[{}]".format(e.graphic), end = "")
            			break
        			else:
          				print("[ ]", end = "")

      	print()
	
	def add_entities(self, entities):
    	self.entities += entities

p = Player(1, 1, "P")
m1 = Monster(3, 4, "M")
m2 = Monster(4, 7, "M")


level = Level(20, 20)

level.add_entities([player, monster])

level.draw()