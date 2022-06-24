#code from moving animations video

import pygame,time, os, random, math, datetime,sys

pygame.init()
WIDTH=900
HEIGHT=600

#fonts
TITLE_FONT = pygame.font.SysFont('comicsans', WIDTH//20)
MENU_FONT = pygame.font.SysFont('comicsans', WIDTH//25)
INSTRUC_FONT = pygame.font.SysFont('comicsans', WIDTH//35)
bx=WIDTH//3
#colors
colors={"white":(255,255,255),"pink":(255,0,255),"blue":(0,0,255),"limeGreen":(153,255,51),"gold":(255,215,0)}
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Temple RUn')

#loading the images into the game
walkRight = [pygame.image.load('pygameFiles\imagesfolder\R1.png'), pygame.image.load('pygameFiles\imagesfolder\R2.png'), pygame.image.load('pygameFiles\imagesfolder\R3.png'), pygame.image.load('pygameFiles\imagesfolder\R4.png'), pygame.image.load('pygameFiles\imagesfolder\R5.png'), pygame.image.load('pygameFiles\imagesfolder\R6.png'), pygame.image.load('pygameFiles\imagesfolder\R7.png'), pygame.image.load('pygameFiles\imagesfolder\R8.png'), pygame.image.load('pygameFiles\imagesfolder\R9.png')]
walkLeft = [pygame.image.load('pygameFiles\imagesfolder\L1.png'), pygame.image.load('pygameFiles\imagesfolder\L2.png'), pygame.image.load('pygameFiles\imagesfolder\L3.png'), pygame.image.load('pygameFiles\imagesfolder\L4.png'), pygame.image.load('pygameFiles\imagesfolder\L5.png'), pygame.image.load('pygameFiles\imagesfolder\L6.png'), pygame.image.load('pygameFiles\imagesfolder\L7.png'), pygame.image.load('pygameFiles\imagesfolder\L8.png'), pygame.image.load('pygameFiles\imagesfolder\L9.png')]
char = pygame.image.load('pygameFiles\imagesfolder\standing.png')
bg=pygame.image.load('pygameFiles\imagesfolder\goodbg.jpg')
bg=pygame.transform.scale(bg,(WIDTH,HEIGHT)) #resizing bg
platform1=pygame.image.load("pygameFiles\imagesfolder\platform.png")
platform1=pygame.transform.scale(platform1,(100,50))
coin1=pygame.image.load('pygameFiles\imagesfolder\coin.png')
coin1=pygame.transform.scale(coin1,(40,40))
treasure=pygame.image.load('pygameFiles\imagesfolder\treasurewobg.png')
treasure=pygame.transform.scale(treasure,(100,80))
#variables
x=0
y=395
width=64
vel=10
isJump=False
jumpCount=10
clock=pygame.time.Clock()
#variables to keep track of image
left = False
right = False
walkCount = 0
#timer variables
current_time=0
button_press_time=0
platform1_rect=pygame.Rect(100,400, 100, 50)
platform2_rect=pygame.Rect(300,300, 100, 50)
platform3_rect=pygame.Rect(500,200, 100, 50)
platform4_rect=pygame.Rect(500,400, 100, 50)
platform5_rect=pygame.Rect(700,300, 100, 50)
hitbox=pygame.Rect(x+5,y+10,50,50) #figure out dimension of character

def level2():
    global walkCount, left, right, x, y, button_press_time, current_time, isJump, jumpCount
    #blitting the background, platforms, and coins to the level
    def redrawwindow():
        global walkCount, x, y
        screen.blit(bg, (0,0))  #background at 0,0
        screen.blit(platform1,(100,400))
        screen.blit(platform1,(270,300))
        screen.blit(platform1,(475,200))
        screen.blit(platform1,(475,400))
        screen.blit(platform1,(660,300))
        screen.blit(coin1,(130,350))
        screen.blit(coin1,(130,150))
        screen.blit(coin1,(505,360))
        screen.blit(coin1,(690,260))
        screen.blit(treasure,(795,375))
        pygame.draw.rect(screen, (255,255,255), hitbox)
        pygame.display.update()
        if walkCount + 1 >= 27: 
            walkCount = 0
        if left:  #displays images that show the sprite moving to the left
            screen.blit(walkLeft[walkCount//3], (x,y))
            walkCount += 1                          
        elif right: #displays images that show the sprite moving to the right
            screen.blit(walkRight[walkCount//3], (x,y))
            walkCount += 1
        else:
            screen.blit(char, (x, y))
            walkCount = 0
        #create hitbox for character 
        

        pygame.display.update() 
    button_press_time = pygame.time.get_ticks()

    #main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #if press on X, the game quits and exits
                pygame.quit()
                sys.exit()
            
        current_time=pygame.time.get_ticks()

        pygame.display.flip()
        clock.tick(27)

        keys = pygame.key.get_pressed() #initializes the pressing of the keyboard
        
        if keys[pygame.K_LEFT] and x > vel: #moves character left
            x -= vel
            hitbox.x = x+5
            left = True
            right = False
        elif keys[pygame.K_RIGHT] and x < WIDTH - vel - width:  #moves character right
            x += vel
            hitbox.x = x+5
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
                hitbox.y = y+10
                jumpCount -= 1
            else: 
                jumpCount = 10
                isJump = False
        if platform1_rect.colliderect(hitbox):
            x=0
            y=395
            hitbox.x= x+5
            hitbox.y= y+10
        if hitbox.colliderect(platform1_rect):
            if platform1_rect.bottom-hitbox.top==0:
                y=400-char.get_height()
                hitbox.y=y+10



        redrawwindow()
        if current_time - button_press_time > 20000: #if the time reaches 20 seconds, run the endgame function
            noTime()
    
            
    
def noTime(): #function if game reaches time limit
    screen.fill(colors.get("white"))
    text2= TITLE_FONT.render("You ran out of Time!!", 1, colors.get("blue"))
    screen.blit(text2,(250,250))
    pygame.display.update()
    #delay
    #run main menu again

level2()
