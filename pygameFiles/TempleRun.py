#Eitan Hahn
#6/21/2022
import pygame, time,os,random, math, datetime,sys
pygame.init()#initialize the pygame package

os.system('cls')
WIDTH=900 #like constant
HEIGHT=600
TITLE_FONT = pygame.font.SysFont('comicsans', WIDTH//20)
MENU_FONT = pygame.font.SysFont('comicsans', WIDTH//25)
INSTRUC_FONT = pygame.font.SysFont('comicsans', WIDTH//35)
bx=WIDTH//3
colors={"white":(255,255,255),"pink":(255,0,255),"blue":(0,0,255),"limeGreen":(153,255,51),"gold":(255,215,0)}
bg=pygame.image.load('pygameFiles\imagesfolder\\forest-hill-game-background-nature-landscape-different-platforms-separated-layers-games-82120706.jpg')
bg=pygame.transform.scale(bg,(WIDTH,HEIGHT))
#create dispay wind with any name y like
screen=pygame.display.set_mode((WIDTH,HEIGHT),pygame.RESIZABLE) 
pygame.display.set_caption("Temple Run")  #change the title of my window
screen.blit(bg,(0,0))
pygame.display.update()
run=True
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
