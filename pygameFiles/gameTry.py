#code from moving animations video

import pygame,time, os, random, math, datetime,sys
from settings import *
from tiles import Tile
pygame.init()
WIDTH=900
HEIGHT=600
#variables to keep track of image
left = False
right = False
walkCount = 0
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
#variables
x=0
y=395
width=64
height=64
vel=10
isJump=False
jumpCount=10
clock=pygame.time.Clock()
test.tile=pygame.sprite.Group(Tile((100,100)200))

while True: 
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
            sys.exit()



class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface((size,size))
        self.rect =  self.image.get_rect(topleft=pos)