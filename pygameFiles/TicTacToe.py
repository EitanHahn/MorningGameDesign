#Eitan Hahn
#tic tac toe game
import pygame, time, os, random, math, datetime, sys
pygame.init()#initialize the pygame package
os.system('cls')
WIDTH=700 #like constant
HEIGHT=700
TITLE_FONT = pygame.font.SysFont('comicsans', WIDTH//20)
MENU_FONT = pygame.font.SysFont('comicsans', WIDTH//25)
colors={"white":(255,255,255),"pink":(255,0,255),"blue":(0,0,255),"limeGreen":(153,255,51),"gold":(255,215,0)}
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

#functions: 
# draw_grid()
# zero_grid()
# draw_marker()
# check_winner()
# game_end()

SIZE=3
markers=[]
MxMy=(0,0)
lineWidth=10
cellx=0
celly=0
player=1
circleColor=colors.get("limeGreen")
xColor=colors.get("gold")

def zero_grid():
    for x in range (SIZE):
        row=[0]*SIZE #this will create 3 zeros
        markers.append(row)
       
#zero_grid()
#print(markers)
#markers[1][1]=-1 #first index is row, second index is column
#print(markers)
#print(markers[1][1])

def draw_grid():
    bgColor=colors.get("pink")
    lineColor=colors.get("blue")
    screen.fill(bgColor)
    for x in range(1,SIZE):
        pygame.draw.line(screen, lineColor, (0, HEIGHT//SIZE*x), (WIDTH, HEIGHT//SIZE*x), lineWidth) #horizontal
        pygame.draw.line(screen, lineColor, (WIDTH//SIZE*x, 0), (WIDTH//SIZE*x, HEIGHT), lineWidth) #vertical
    pygame.display.update()
   
def draw_Markers():
    xValue=0
    for x in markers: #give me each row of the list
        yValue=0
        for y in x:
            if y==1:
                #draw X
                pygame.draw.line(screen, xColor,(xValue*WIDTH//3+15, yValue*HEIGHT//3+15),(xValue*WIDTH//3+WIDTH//3,yValue*HEIGHT-15),(lineWidth))
            if y==-1:
                #draw O
                pygame.draw.circle(screen, circleColor, (xValue*WIDTH//3+WIDTH//6, yValue*HEIGHT//3+HEIGHT//6 ), WIDTH//6-25, lineWidth)
                yValue+=1
            xValue+=1

def check_end(): #check winner


zero_grid()

Game=True
while Game:
    draw_grid()
    draw_Markers()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            MxMy=pygame.mouse.get_pos
            cellx=MxMy[0]//(WIDTH//SIZE)
            celly=MxMy[1]//(HEIGHT//SIZE)
            print(cellx, celly)
            print(markers)
            if markers[cellx][celly]==0:
                markers[cellx][celly]=player
                player*=-1
    pygame.time.delay(50)
    pygame.display.update