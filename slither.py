import pygame
import random

pygame.init()

white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,155,0)

display_width=800
display_height=600 

gameDisplay=pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption("Slither")

img=pygame.image.load('snakeHead.png')


block_size=20
FPS=15
direction="right"

#clock
clock=pygame.time.Clock()

#font object
font=pygame.font.SysFont(None,25)

def text_object(text,color):
	textSurface=font.render(text,True,color)
	return textSurface, textSurface.get_rect()
	

def message_to_screen(msg,color,y_displace=0):
	textSurf, textRect=text_object(msg,color)
	textRect.center=(display_width/2,display_height/2 ++y_displace)
	gameDisplay.blit(textSurf, textRect)
	
def score(scores):
	text=font.render("Score: "+str(scores),True,black)
	gameDisplay.blit(text,[10,10])
	
def snake(block_size,snakeList):
	head=img
	if direction=="right":
		head=pygame.transform.rotate(img,270)
	if direction=="left":
		head=pygame.transform.rotate(img,90)
	if direction=="up":
		head=img
	if direction=="down":
		head=pygame.transform.rotate(img,180)
	
	gameDisplay.blit(head,(snakeList[-1][0],snakeList[-1][1]))
	for xny in snakeList[:-1]:
		pygame.draw.rect(gameDisplay,green,[xny[0],xny[1],block_size ,block_size])  #topleft corner, width and height


def gameLoop():
	global direction
	gameExit=False
	gameOver=False
	lead_x_change=10
	lead_y_change=0
	lead_x=display_width/2
	lead_y=display_height/2
	snakeList1=[]
	snakeLength=1;
	
	randAppleX=round(random.randrange(0,display_width-block_size))
	randAppleY=round(random.randrange(0,display_height-block_size))

	while not gameExit:
		while gameOver==True:
			gameDisplay.fill(white)
			message_to_screen("Game Over",red,y_displace=-50)
			message_to_screen("Score: "+str(snakeLength-1),black,0)
			message_to_screen("Press C to play again or Q to quit",black,50)
			
			pygame.display.update()
			for event in pygame.event.get():
				if event.type==pygame.QUIT:
					gameExit=True
					gameOver=False
				if event.type==pygame.KEYDOWN:
					if event.key==pygame.K_q:
						gameExit=True
						gameOver=False
					elif event.key==pygame.K_c:
						gameLoop()
			
			
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				gameExit=True
				gameOver=False
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_LEFT:
					direction="left"
					lead_x_change=-block_size  #moving by the thickness or size of box(snake)
					lead_y_change=0
				elif event.key==pygame.K_RIGHT:
					direction="right"
					lead_x_change=block_size 
					lead_y_change=0
				elif event.key==pygame.K_UP:
					direction="up"
					lead_y_change=-block_size 
					lead_x_change=0
				elif event.key==pygame.K_DOWN:
					direction="down"
					lead_y_change=block_size 
					lead_x_change=0
			if event.type==pygame.KEYUP:
				if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
					lead_x_change=0
				elif event.key==pygame.K_UP or event.key==pygame.K_DOWN:
					lead_y_change=0
		
		
		
		if lead_x>=display_width or lead_x<0 or lead_y>=display_height or lead_y<=0:
			gameOver=True
		
		lead_x+=lead_x_change
		lead_y+=lead_y_change
		
		gameDisplay.fill(white)
		appleThickness=30
		pygame.draw.rect(gameDisplay,red,[randAppleX, randAppleY,appleThickness,appleThickness])
		#pygame.draw.rect(gameDisplay,green,[lead_x,lead_y,block_size ,block_size ])  #topleft corner, width and height
		
		
		snakeHead=[]
		snakeHead.append(lead_x)
		snakeHead.append(lead_y)
		
		snakeList1.append(snakeHead)
		
		
		if len(snakeList1)>snakeLength:
			del snakeList1[0]
	
		
		if snakeHead in snakeList1[:-1]:
			gameOver=True;
		
			
		snake(block_size,snakeList1)
		score(snakeLength-1)
		pygame.display.update()


		if lead_x >randAppleX and lead_x<randAppleX+appleThickness or lead_x + block_size >randAppleX and lead_x+block_size<randAppleX+appleThickness:
			if lead_y >randAppleY and lead_y<randAppleY +appleThickness or lead_y + block_size >randAppleY and lead_y+block_size<randAppleY+appleThickness:
				randAppleX=round(random.randrange(0,display_width-block_size))
				randAppleY=round(random.randrange(0,display_height-block_size))
				snakeLength+=1
		
		clock.tick(FPS) #specify frame per sec required
			

	pygame.quit()
	quit()
	
gameLoop()



