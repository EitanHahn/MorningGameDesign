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
pygame.display.set_caption('Treasure Run')

#loading the images into the game
walkRight = [pygame.image.load('pygameFiles\imagesfolder\R1.png'), pygame.image.load('pygameFiles\imagesfolder\R2.png'), pygame.image.load('pygameFiles\imagesfolder\R3.png'), pygame.image.load('pygameFiles\imagesfolder\R4.png'), pygame.image.load('pygameFiles\imagesfolder\R5.png'), pygame.image.load('pygameFiles\imagesfolder\R6.png'), pygame.image.load('pygameFiles\imagesfolder\R7.png'), pygame.image.load('pygameFiles\imagesfolder\R8.png'), pygame.image.load('pygameFiles\imagesfolder\R9.png')]
walkLeft = [pygame.image.load('pygameFiles\imagesfolder\L1.png'), pygame.image.load('pygameFiles\imagesfolder\L2.png'), pygame.image.load('pygameFiles\imagesfolder\L3.png'), pygame.image.load('pygameFiles\imagesfolder\L4.png'), pygame.image.load('pygameFiles\imagesfolder\L5.png'), pygame.image.load('pygameFiles\imagesfolder\L6.png'), pygame.image.load('pygameFiles\imagesfolder\L7.png'), pygame.image.load('pygameFiles\imagesfolder\L8.png'), pygame.image.load('pygameFiles\imagesfolder\L9.png')]
char = pygame.image.load('pygameFiles\imagesfolder\standing.png')
bg=pygame.image.load('pygameFiles\imagesfolder\goodbg.jpg')
bg=pygame.transform.scale(bg,(WIDTH,HEIGHT)) #resizing bg
platform1=pygame.image.load("pygameFiles\imagesfolder\\rightspikes.png")
platform1=pygame.transform.scale(platform1,(100,60))
coin1=pygame.image.load('pygameFiles\imagesfolder\coinwobg.png')
coin1=pygame.transform.scale(coin1,(40,40))
coin2=pygame.image.load('pygameFiles\imagesfolder\coinwobg.png')
coin2=pygame.transform.scale(coin2,(40,40))
coin3=pygame.image.load('pygameFiles\imagesfolder\coinwobg.png')
coin3=pygame.transform.scale(coin3,(40,40))
coin4=pygame.image.load('pygameFiles\imagesfolder\coinwobg.png')
coin4=pygame.transform.scale(coin4,(40,40))
treasure=pygame.image.load('pygameFiles\imagesfolder\\treasurewobg.png')
treasure=pygame.transform.scale(treasure,(100,80))
score=0
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
platform2_rect=pygame.Rect(250,200, 100, 50)
platform3_rect=pygame.Rect(475,150, 100, 50)
platform4_rect=pygame.Rect(475,400, 100, 50)
platform5_rect=pygame.Rect(660,330, 100, 50)
hitbox=pygame.Rect(x+5,y+10,40,40) #figure out dimension of character
coin1_rect=pygame.Rect(130,250,40,40)
coin2_rect=pygame.Rect(270,390,40,40)
coin3_rect=pygame.Rect(505,285,40,40)
coin4_rect=pygame.Rect(690,200,40,40)
treasure_rect=pygame.Rect(795,375,100,80)

def level2():
    global walkCount, left, right,x, y, button_press_time, current_time, isJump, jumpCount, coin1, coin2, coin3, coin4, score, coin1_rect, coin2_rect, coin3_rect, coin4_rect
    #loading the images into the game
    walkRight = [pygame.image.load('pygameFiles\imagesfolder\R1.png'), pygame.image.load('pygameFiles\imagesfolder\R2.png'), pygame.image.load('pygameFiles\imagesfolder\R3.png'), pygame.image.load('pygameFiles\imagesfolder\R4.png'), pygame.image.load('pygameFiles\imagesfolder\R5.png'), pygame.image.load('pygameFiles\imagesfolder\R6.png'), pygame.image.load('pygameFiles\imagesfolder\R7.png'), pygame.image.load('pygameFiles\imagesfolder\R8.png'), pygame.image.load('pygameFiles\imagesfolder\R9.png')]
    walkLeft = [pygame.image.load('pygameFiles\imagesfolder\L1.png'), pygame.image.load('pygameFiles\imagesfolder\L2.png'), pygame.image.load('pygameFiles\imagesfolder\L3.png'), pygame.image.load('pygameFiles\imagesfolder\L4.png'), pygame.image.load('pygameFiles\imagesfolder\L5.png'), pygame.image.load('pygameFiles\imagesfolder\L6.png'), pygame.image.load('pygameFiles\imagesfolder\L7.png'), pygame.image.load('pygameFiles\imagesfolder\L8.png'), pygame.image.load('pygameFiles\imagesfolder\L9.png')]
    char = pygame.image.load('pygameFiles\imagesfolder\standing.png')
    bg=pygame.image.load('pygameFiles\imagesfolder\goodbg.jpg')
    bg=pygame.transform.scale(bg,(WIDTH,HEIGHT)) #resizing bg
    platform1=pygame.image.load("pygameFiles\imagesfolder\\rightspikes.png")
    platform1=pygame.transform.scale(platform1,(100,60))
    coin1=pygame.image.load('pygameFiles\imagesfolder\coinwobg.png')
    coin1=pygame.transform.scale(coin1,(40,40))
    coin2=pygame.image.load('pygameFiles\imagesfolder\coinwobg.png')
    coin2=pygame.transform.scale(coin2,(40,40))
    coin3=pygame.image.load('pygameFiles\imagesfolder\coinwobg.png')
    coin3=pygame.transform.scale(coin3,(40,40))
    coin4=pygame.image.load('pygameFiles\imagesfolder\coinwobg.png')
    coin4=pygame.transform.scale(coin4,(40,40))
    treasure=pygame.image.load('pygameFiles\imagesfolder\\treasurewobg.png')
    treasure=pygame.transform.scale(treasure,(100,80))
    score=0
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
    platform2_rect=pygame.Rect(250,200, 100, 50)
    platform3_rect=pygame.Rect(475,150, 100, 50)
    platform4_rect=pygame.Rect(475,400, 100, 50)
    platform5_rect=pygame.Rect(660,330, 100, 50)
    hitbox=pygame.Rect(x+5,y+10,40,40) #figure out dimension of character
    coin1_rect=pygame.Rect(130,250,40,40)
    coin2_rect=pygame.Rect(270,390,40,40)
    coin3_rect=pygame.Rect(505,285,40,40)
    coin4_rect=pygame.Rect(690,200,40,40)
    treasure_rect=pygame.Rect(795,375,100,80)

    
    #blitting the background, platforms, and coins to the level
    def redrawwindow():
        global walkCount, x, y
        screen.blit(bg, (0,0))  #background at 0,0
        screen.blit(platform1,(100,400))
        screen.blit(platform1,(250,200))
        screen.blit(platform1,(475,150))
        screen.blit(platform1,(475,400))
        screen.blit(platform1,(660,330))
        screen.blit(coin1,(130,250))
        screen.blit(coin2,(270,390))
        screen.blit(coin3,(505,285))
        screen.blit(coin4,(690,200))
        screen.blit(treasure,(795,375))
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
                hitbox.y = y
                jumpCount -= 1
            else: 
                jumpCount = 10
                isJump = False
        if platform1_rect.colliderect(hitbox):
            x=0
            y=395
            hitbox.x= x+5
            hitbox.y= y
        if platform2_rect.colliderect(hitbox):
            x=0
            y=250
            hitbox.x= x+5
            hitbox.y= y
        if platform3_rect.colliderect(hitbox):
            x=0
            y=395
            hitbox.x= x+5
            hitbox.y= y
        if platform4_rect.colliderect(hitbox):
            x=0
            y=395
            hitbox.x= x+5
            hitbox.y= y
        if platform5_rect.colliderect(hitbox):
            x=0
            y=340
            hitbox.x= x+5
            hitbox.y= y
        if hitbox.colliderect(treasure_rect):
            endGameL2()


        if coin1_rect.colliderect(hitbox):
            coin1 = pygame.Surface((24, 24), flags=pygame.SRCALPHA)
            coin1.fill((0, 0, 0, 0)) #RGBA sequence
            coin1_rect=pygame.Rect(0,0,40,40)
            score+=1
            print(score)
        if coin2_rect.colliderect(hitbox):
            coin2 = pygame.Surface((24, 24), flags=pygame.SRCALPHA)
            coin2.fill((0, 0, 0, 0)) #RGBA sequence
            coin2_rect=pygame.Rect(0,0,40,40)
            score+=1
            print(score)
        if coin3_rect.colliderect(hitbox):
            coin3 = pygame.Surface((24, 24), flags=pygame.SRCALPHA)
            coin3.fill((0, 0, 0, 0)) #RGBA sequence
            coin3_rect=pygame.Rect(0,0,40,40)
            score+=1
            print(score)
        if coin4_rect.colliderect(hitbox):
            coin4 = pygame.Surface((24, 24), flags=pygame.SRCALPHA)
            coin4.fill((0, 0, 0, 0)) #RGBA sequence
            coin4_rect=pygame.Rect(0,0,40,40)
            score+=1
            print(score)
        
            


#how to only change the height when the character collides with the TOP of the platform
#how to make it so that the user can go off the platform and lower then the height



        redrawwindow()
        if current_time - button_press_time > 20000: #if the time reaches 20 seconds, run the endgame function
            noTimeL2()
    
            
    
def noTimeL2(): #function if game reaches time limit
    screen.fill(colors.get("white"))
    text2= TITLE_FONT.render("You ran out of Time!!", 1, colors.get("blue"))
    screen.blit(text2,(240,250))
    pygame.display.update()
    pygame.time.delay(1000)
    #mainMenu()
def endGameL2():
    screen.fill(colors.get("white"))
    text2= MENU_FONT.render("Congratulations! You reached the Treasure", 1, colors.get("blue"))
    screen.blit(text2,(100,250))
    pygame.display.update()
    pygame.time.delay(1000)
    #mainMenu()



level2()
