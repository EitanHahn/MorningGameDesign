#Eitan Hahn
#6/9/2022
#We are learning about pygame basic functions, creating screens, colors, and shapes
# move
#move the square
#K_UP                  up arrow
#K_DOWN                down arrow
#K_RIGHT               right arrow
#K_LEFT                left arrow
#K_INSERT              insert
#picture=pygame.image.load('filename')
#picture=pygame.transform.scale(variables)

import pygame, time, os, random, math
pygame.init() #initialize the pygame package
os.system('cls')
WIDTH=700 #like constant
HEIGHT=700
colors={"white":(255,255,255),"pink":(255,0,255),"blue":(0,0,255),"limeGreen":(153,255,51)}
Color=colors.get("white")
#create display windowwith any name
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("my first game") #changes the title of the window

#images
bg=pygame.image.load('pygameFiles\imagesfolder\\bgSmaller.jpg')
char=pygame.image.load('pygameFiles\imagesfolder\PixelArtTutorial.png')
char=pygame.transform.scale(char,(80,80))
#screen.blit(bg,(0,0))
#pygame.display.update()
pygame.time.delay(2000)

#variables
hb=50
wb=50
xb=100
yb=300


mountainSquare = pygame.Rect(250, 320, 180, 250)

charx=350
chary=100


cx=350
cy=350
rad=25
ibox=rad*math.sqrt(2)
xig = cx-(ibox/2)
yig = cy-(ibox/2)

square=pygame.Rect(xb,yb,wb,hb) #creates the object
insSquare=pygame.Rect(xig, yig, ibox, ibox)
squareColor=colors.get("pink")
#to keep running, create a loop
circleColor=colors.get("blue")
run= True
background=Color=colors.get("white")
triangleColor=colors.get("limeGreen")
#create variable to move
speed=2


while run:
    screen.blit(bg,(0,0))
    #screen.fill(background)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            print("You Quit")

    keys=pygame.key.get_pressed() #this is a list
    #move square
    if keys [pygame.K_RIGHT] and square.x < WIDTH - (wb+speed):
        square.x += speed
        charx+=speed
    if keys [pygame.K_LEFT] and square.x > speed:
        square.x -= speed
        charx-=speed
    if keys [pygame.K_UP] and square.y > speed:  #up means closer to 0, so its subtraction
        square.y -= speed
        chary-=speed
    if keys [pygame.K_DOWN] and square.y < HEIGHT-hb:#down is closer to maximum value, so its addition
        square.y += speed
        chary+=speed
    #move circle
    if keys [pygame.K_d] and cx < WIDTH - (rad):
        cx += speed
        insSquare.x += speed
    if keys [pygame.K_a] and cx > (speed+rad):
        cx -= speed
        insSquare.x -= speed
    if keys [pygame.K_w] and cy > (speed+rad): 
        cy -= speed
        insSquare.y -= speed
    if keys [pygame.K_s] and cy < HEIGHT-(rad):
        cy += speed
        insSquare.y += speed
    if square.colliderect(insSquare):
        print('BOOM') 
        rad+=5
        cx=random.randint(rad, WIDTH-rad)
        cy=random.randint(rad, HEIGHT-rad)
        ibox=rad*math.sqrt(2)
        xig = cx-(ibox/2)
        yig = cy-(ibox/2)
        insSquare=pygame.Rect(xig, yig, ibox, ibox)
     #mountain collide square
    if square.colliderect(mountainSquare):
        square.x = 10
        square.y = 10
        charx = 10
        chary = 10
    
    #mountain collide circle
    if insSquare.colliderect(mountainSquare):
        cx = rad + 10
        cy = rad + 10
        ibox = rad*math.sqrt(2)
        xig = cx-(ibox/2)
        yig = cy-(ibox/2)
        insSquare=pygame.Rect(xig,yig,ibox,ibox)

    #rect(surface, color, rect)
    pygame.draw.rect(screen, squareColor, square)
    #circle(surface, color, center, radius)
    pygame.draw.circle(screen, circleColor, (cx,cy),rad)
    screen.blit(char,(charx, chary))
    pygame.draw.polygon (screen, triangleColor, [(500,500),(350,400),(600,650)])
    pygame.draw.rect(screen, squareColor, insSquare,)
    pygame.display.update()

