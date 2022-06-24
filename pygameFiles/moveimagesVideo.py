#code from moving animations video

from importlib.abc import TraversableResources
import pygame
pygame.init

#variables to keep track of image
left = False
right = False
walkCount = 0

screen=pygame.display.set_mode((500,480))
pygame.display.set_caption('Moving Animations')

#loading the images into the game
walkRight = [pygame.image.load('pygameFiles\imagesfolder\R1.png'), pygame.image.load('pygameFiles\imagesfolder\R2.png'), pygame.image.load('pygameFiles\imagesfolder\R3.png'), pygame.image.load('pygameFiles\imagesfolder\R4.png'), pygame.image.load('pygameFiles\imagesfolder\R5.png'), pygame.image.load('pygameFiles\imagesfolder\R6.png'), pygame.image.load('pygameFiles\imagesfolder\R7.png'), pygame.image.load('pygameFiles\imagesfolder\R8.png'), pygame.image.load('pygameFiles\imagesfolder\R9.png')]
walkLeft = [pygame.image.load('pygameFiles\imagesfolder\L1.png'), pygame.image.load('pygameFiles\imagesfolder\L2.png'), pygame.image.load('pygameFiles\imagesfolder\L3.png'), pygame.image.load('pygameFiles\imagesfolder\L4.png'), pygame.image.load('pygameFiles\imagesfolder\L5.png'), pygame.image.load('pygameFiles\imagesfolder\L6.png'), pygame.image.load('pygameFiles\imagesfolder\L7.png'), pygame.image.load('pygameFiles\imagesfolder\L8.png'), pygame.image.load('pygameFiles\imagesfolder\L9.png')]
char = pygame.image.load('pygameFiles\imagesfolder\standing.png')
bg=pygame.image.load('pygameFiles\imagesfolder\\forest-hill-game-background-nature-landscape-different-platforms-separated-layers-games-82120706.jpg')
#variables
x=50
y=400
width=40
height=60
vel=5
isJump=False
jumpCount=10
clock=pygame.time.Clock()

def redrawGameWindow():
    global walkCount
    
    screen.blit(bg, (0,0))  #background at 0,0
    if walkCount + 1 >= 27:
        walkCount = 0
        
    if left:  
        screen.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1                          
    elif right:
        screen.blit(walkRight[walkCount//3], (x,y))
        walkCount += 1
    else:
        screen.blit(char, (x, y))
        walkCount = 0
        
    pygame.display.update() 

#main loop
run=True
while run:
    clock.tick(27)
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x > vel: #moves character left
        x -= vel
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < 500 - vel - width:  #moves character right
        x += vel
        left = False
        right = True
        
    else: # character not moving, left and right must equal false and walkcount 0
        left = False
        right = False
        walkCount = 0
        
    if not(isJump): #jumping
        if keys[pygame.K_SPACE]:
            isJump = True
            right = False 
            left = False 
            walkCount = 0
    else:
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else: 
            jumpCount = 10
            isJump = False

    redrawGameWindow() 
    
    
pygame.quit()