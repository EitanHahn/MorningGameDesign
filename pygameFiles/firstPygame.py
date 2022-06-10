#Eitan Hahn
#6/9/2022
#We are learning about pygame basic functions, creating screens, colors, and shapes

import pygame, time, os
pygame.init() #initialize the pygame package
os.system('cls')
WIDTH=700 #like constant
HEIGHT=700
#create display windowwith any name
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("my first game") #changes the title of the window
pygame.time.delay(2000)
redColor=(250,0,0)
#screen.fill(redColor)
#pygame.display.update()
#pygame.time.delay(2000)
greenColor=(0,255,0)
purpleColor=(125,0,125)
blueColor=(0,0,250)
#screen.fill(greenColor)
#pygame.display.update()
#pygame.time.delay(2000)
hb=50
wb=50
xb=100
yb=300
square=(xb,yb,wb,hb) #creates the object
#to keep running, create a loop
run= True
background=greenColor
while run:
    screen.fill(background)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            print("You Quit")
    #rect(surface, color, rect)
    pygame.draw.rect(screen, redColor, square)
    #circle(surface, color, center, radius)
    pygame.draw.circle(screen, purpleColor, (350,350),25)
    pygame.draw.polygon (screen, blueColor, [(500,500),(350,400),(600,650)])
    pygame.display.update()

