#Eitan Hahn
#6/21/2022
import pygame, time,os,random, math, datetime,sys
pygame.init()#initialize the pygame package

os.system('cls')
WIDTH=900 #like constant
HEIGHT=600
#fonts
TITLE_FONT = pygame.font.SysFont('comicsans', WIDTH//20)
MENU_FONT = pygame.font.SysFont('comicsans', WIDTH//25)
INSTRUC_FONT = pygame.font.SysFont('comicsans', WIDTH//35)
bx=WIDTH//3
#colors
colors={"white":(255,255,255),"pink":(255,0,255),"blue":(0,0,255),"limeGreen":(153,255,51),"gold":(255,215,0)}
#images
bg=pygame.image.load('pygameFiles\imagesfolder\\forest-hill-game-background-nature-landscape-different-platforms-separated-layers-games-82120706.jpg')
bg=pygame.transform.scale(bg,(WIDTH,HEIGHT))
walkRight = [pygame.image.load('pygameFiles\imagesfolder\R1.png'), pygame.image.load('pygameFiles\imagesfolder\R2.png'), pygame.image.load('pygameFiles\imagesfolder\R3.png'), pygame.image.load('pygameFiles\imagesfolder\R4.png'), pygame.image.load('pygameFiles\imagesfolder\R5.png'), pygame.image.load('pygameFiles\imagesfolder\R6.png'), pygame.image.load('pygameFiles\imagesfolder\R7.png'), pygame.image.load('pygameFiles\imagesfolder\R8.png'), pygame.image.load('pygameFiles\imagesfolder\R9.png')]
walkLeft = [pygame.image.load('pygameFiles\imagesfolder\L1.png'), pygame.image.load('pygameFiles\imagesfolder\L2.png'), pygame.image.load('pygameFiles\imagesfolder\L3.png'), pygame.image.load('pygameFiles\imagesfolder\L4.png'), pygame.image.load('pygameFiles\imagesfolder\L5.png'), pygame.image.load('pygameFiles\imagesfolder\L6.png'), pygame.image.load('pygameFiles\imagesfolder\L7.png'), pygame.image.load('pygameFiles\imagesfolder\L8.png'), pygame.image.load('pygameFiles\imagesfolder\L9.png')]
char = pygame.image.load('pygameFiles\imagesfolder\standing.png')
#create dispay name
screen=pygame.display.set_mode((WIDTH,HEIGHT),pygame.RESIZABLE) 
pygame.display.set_caption("Temple Run")  #change the title of my window
screen.blit(bg,(0,0))
pygame.display.update()

bg_img = pygame.image.load('pygameFiles\imagesfolder\\forest-hill-game-background-nature-landscape-different-platforms-separated-layers-games-82120706.jpg')
bg_img = pygame.transform.scale(bg_img,(WIDTH,HEIGHT))
 
i = 0
 
runing = True
while runing:
    screen.fill((0,0,0))
    screen.blit(bg_img,(i,0))
    screen.blit(bg_img,(WIDTH+i,0))
    if (i==-WIDTH):
        screen.blit(bg_img,(WIDTH+i,0))
        i=0
    i-=1
    for event in pygame.event.get():
        if event.type == quit:
            runing = False
            pygame.display.update()
            pygame.quit()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
