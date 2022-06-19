import pygame
import random
import time

pygame.init()


########### ZMIENNE ##################
grid_size = 50
screen_size = (grid_size*15,grid_size*15)
screen = pygame.display.set_mode(screen_size)


how_many_grids_x = int(screen_size[0]/grid_size)
how_many_grids_y = int(screen_size[1]/grid_size)

clock = pygame.time.Clock()
Not_Closed = True


############### KLASY ####################

class food(pygame.sprite.Sprite):
	def __init__(self,screen,how_many_grids_x,how_many_grids_y,grid_size):
		self.how_many_grids_x = how_many_grids_x
		self.how_many_grids_y = how_many_grids_y
		self.grid_size = grid_size
		self.screen = screen
		self.x = random.randint(0,self.how_many_grids_x-1)
		self.y = random.randint(0,self.how_many_grids_y-1)
		self.positions = [(self.x,self.y)]
		pygame.draw.rect(screen,(200,10,10),((self.x*self.grid_size,self.y*self.grid_size),(self.grid_size,self.grid_size)))

	def draw(self):
		pygame.draw.rect(screen,(200,10,10),((self.x*self.grid_size,self.y*self.grid_size),(self.grid_size,self.grid_size)))
	def random_pos(self):
		self.x = random.randint(0,self.how_many_grids_x-1)
		self.y = random.randint(0,self.how_many_grids_y-1)
	def update(self):
		self.positions = [(self.x,self.y)]
		self.draw()

class snake(pygame.sprite.Sprite):
	def __init__(self,screen,Not_Closed):


		self.L = (-1,0)
		self.R = (1,0)
		self.U = (0,-1)
		self.D = (0,1)
		self.directions = self.R
		self.positions = [(1,1)]
		self.lenght = 1
		self.screen = screen
		self.Not_Closed = Not_Closed

	def turn(self,where):
		if self.lenght>1 and ((where[0] * -1),(where[1]* -1)) == self.directions:
			return
		else:
			self.directions = where


	def keys(self):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_a]:
			self.turn(self.L)
		if keys[pygame.K_d]:
			self.turn(self.R)
		if keys[pygame.K_w]:
			self.turn(self.U)
		if keys[pygame.K_s]:
			self.turn(self.D)

	def move(self):

		self.old = self.positions[0]
		#print(self.old)
		#print(self.directions)
		self.new = ((self.old[0]+self.directions[0],self.old[1]+self.directions[1]))
		self.positions.insert(0,self.new)
		if len(self.positions)>self.lenght:
			self.positions.pop()




	def draw(self):
		for p in self.positions:
			#print(p)
			r = random.randint(20,50)
			r2 = random.randint(20,200)
			r3 = random.randint(20,200)
			pygame.draw.rect(screen,(r,r2,r3),pygame.Rect(p[0]*grid_size,p[1]*grid_size,grid_size,grid_size))

	def update(self):
		self.keys()
		#print(self.directions)
		self.move()
		self.draw()
		if self.lenght > 1:
			for i in self.positions[2:]:
				if self.new == i:
					print("bruh moments")
					self.Not_Closed = False
		if self.new[0] < 0 or self.new[0]>how_many_grids_x-1:
			self.Not_Closed = False
		elif self.new[1] < 0 or self.new[1]>how_many_grids_y-1:
			self.Not_Closed = False



food = food(screen,how_many_grids_x,how_many_grids_y,grid_size)
snake = snake(screen,True)

			 
############### FUNKCJE #################

def painting(screen,screen_size,grid_size):
	screen.fill((100,50,25))

	for i in range(how_many_grids_x):
		pygame.draw.rect(screen,(1,1,1),((grid_size*i,0),(1,screen_size[1]))) #ekran,kolor,(x,y lewego gornego rogu, szerokość)
	for i in range(how_many_grids_y):
		pygame.draw.rect(screen,(1,1,1),((0,grid_size*i),(screen_size[0],1))) # tak samo





while Not_Closed == True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			Not_Closed = False

	if food.positions[0] == snake.positions[0]:
		snake.lenght += 1
		food.random_pos()
	painting(screen,screen_size,grid_size)
	food.update()
	snake.update()
	#print(snake.positions)
	print(len(snake.positions))
	if snake.Not_Closed == Not_Closed:
		pass
	else:
		Not_Closed = False





	pygame.display.update()
	clock.tick(8)
