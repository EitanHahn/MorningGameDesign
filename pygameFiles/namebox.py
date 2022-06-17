#Eitan Hahn
#6/17/22
#get user name in pygame

import pygame, sys, os

pygame.init()
os.system('cls')
colors={"white":(255,255,255),"pink":(255,0,255),"blue":(0,0,255),"limeGreen":(153,255,51),"gold":(255,215,0)}
clock = pygame.time.Clock()
backgrnd=(255,255,255)
WIDTH=600
HEIGHT=600
xd=WIDTH//3
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Get Name")
screen.fill(backgrnd)
run=True #to run the while loop
user_name=''
nameClr=(0,105,105) #for the text of the name
boxClr= (200,200,200) #for the text box
TITLE_FONT = pygame.font.SysFont('comicsans', WIDTH//20)
MENU_FONT = pygame.font.SysFont('comicsans', WIDTH//25)
title=TITLE_FONT.render("Enter Name",1,boxClr)
screen.blit(title,(200,50)) 
input_rect = pygame.Rect((WIDTH//3, HEIGHT//3), (140, 40))

#make box
while run:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            #Menu(mainTitle,messageMenu)
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print()
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_RETURN:  
                print("name is in")
                #run main menu
                pygame.quit()
                sys.exit()
            if event.key==pygame.K_BACKSPACE:
                user_name=user_name[:-1]
            else:
                user_name+=event.unicode
        pygame.draw.rect(screen, boxClr, input_rect)
        
        text_surface = MENU_FONT.render(user_name, True, nameClr)
        #use your x,y
        screen.blit(text_surface,(input_rect.x+5,input_rect.y+5))

        pygame.display.flip()
