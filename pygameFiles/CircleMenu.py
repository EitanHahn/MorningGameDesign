#Eitan Hahn
#6/13/2022
#We are learning pygame basic functins, 
# creating the menu and instructions
import pygame, time,os,random, math, datetime,sys
pygame.init()#initialize the pygame package

# print(pygame.font.get_fonts())
# pygame.time.delay(10000)
TITLE_FONT = pygame.font.SysFont('comicsans', 40)
MENU_FONT = pygame.font.SysFont('comicsans', 20)

os.system('cls')
WIDTH=700 #like constant
HEIGHT=700
TITLE_FONT = pygame.font.SysFont('comicsans', WIDTH//20)
MENU_FONT = pygame.font.SysFont('comicsans', WIDTH//25)
colors={"white":(255,255,255),"pink":(255,0,255),"blue":(0,0,255),"limeGreen":(153,255,51),"gold":(255,215,0)}
clr=colors.get("limeGreen")

message=["Instructions", "Settings", "Game 1", "Game 2", "Scoreboard", "Exit"]
settingsList=["Background color","Screen size","Sound ON/OFF"]
#create dispay wind with any name y like
screen=pygame.display.set_mode((WIDTH,HEIGHT),pygame.RESIZABLE) 
pygame.display.set_caption("My First Game")  #change the title of my window

clock=pygame.time.Clock()
#images
bg=pygame.image.load('pygameFiles\imagesfolder\\bgSmaller.jpg')
char = pygame.image.load('PygameFiles\imagesfolder\PixelArtTutorial.png')
char = pygame.transform.scale(char, (50, 50))
# screen.blit(bg, (0,0))
# pygame.display.update()
# pygame.time.delay(5000)


#square Var
hb=50
wb=50
xb=100
yb=300

charx = xb
chary = yb

cx=350
cy=350
rad=25
speed=2
ibox = rad*math.sqrt(2)
xig = cx-(ibox/2)
yig = cy-(ibox/2)

#mouse varuables
mx = 0
my = 0

square=pygame.Rect(xb,yb,wb,hb)# create the object to draw
insSquare=pygame.Rect(xig,yig,ibox,ibox)
squareClr=colors.get("pink")
#keep running create a lp
circleClr=colors.get("blue")
backgrnd=colors.get("white")
run = True
Game = False
xd=WIDTH//2
def name():
    xd=WIDTH//3
    screen.fill(backgrnd)
    run=True #to run the while loop
    user_name=''
    nameClr=(0,105,105) #for the text of the name
    boxClr= (200,200,200) #for the text box
    title=TITLE_FONT.render("Enter Name",1,boxClr)
    screen.blit(title,(200,50)) 
    input_rect = pygame.Rect((WIDTH//3, HEIGHT//3), (140, 40))

    #make box
    while run:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                #Menu(mainTitle,messageMenu)
                Mainmenu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                print()
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:  
                    print("your name is " + user_name)
                    #run main menu
                    Mainmenu()
                if event.key==pygame.K_BACKSPACE:
                    user_name=user_name[:-1]
                else:
                    user_name+=event.unicode
            pygame.draw.rect(screen, boxClr, input_rect)
            
            text_surface = MENU_FONT.render(user_name, True, nameClr)
            #use your x,y
            screen.blit(text_surface,(input_rect.x+5,input_rect.y+5))

            pygame.display.flip()
            clock.tick(60)

def Mainmenu():
    Title = TITLE_FONT.render("Circle eats Square", 1, colors.get("blue"))
    screen.fill(colors.get("white"))
    xd = WIDTH//2.5 
    screen.blit(Title, (xd, 50))
    xd=WIDTH//2
    yMenu=155
    ByeBye = TITLE_FONT.render("ByeBye", 1, colors.get("blue"))
    Button_Instructions= pygame.Rect((xd, 150), (WIDTH//4, 40))
    Button_Settings = pygame.Rect((xd, 200), (WIDTH//4, 40))
    Button_Game1 = pygame.Rect((xd, 250), (WIDTH//4, 40))
    Button_Game2 = pygame.Rect((xd, 300), (WIDTH//4, 40))
    Button_Scoreboard = pygame.Rect((xd, 350), (WIDTH//4, 40))
    Button_Exit = pygame.Rect((xd, 400), (WIDTH//4, 40))
    pygame.draw.rect(screen, colors.get("pink"), Button_Instructions)
    pygame.draw.rect(screen, colors.get("limeGreen"), Button_Settings)
    pygame.draw.rect(screen, colors.get("gold"), Button_Game1)
    pygame.draw.rect(screen, colors.get("pink"), Button_Game2)
    pygame.draw.rect(screen, colors.get("limeGreen"), Button_Scoreboard)
    pygame.draw.rect(screen, colors.get("gold"), Button_Exit)
    for item in message:
        text=MENU_FONT.render(item, 1, colors.get('blue'))
        screen.blit(text, (xd, yMenu))
        pygame.display.update()
        yMenu += 50
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                mx = mousePos[0]
                my = mousePos[1]
                if Button_Instructions.collidepoint((mx, my)):
                    Instructions()
                if Button_Settings.collidepoint((mx, my)):
                    settings()
                if Button_Game1.collidepoint((mx, my)):
                    Game1()
                if Button_Game2.collidepoint((mx, my)):
                    Game2()
                if Button_Scoreboard.collidepoint((mx,my)):
                    scoreboard()
                if Button_Exit.collidepoint((mx,my)):
                    run=False
                    event.type==pygame.quit()

                     
def Instructions():
    #rendering text objects
    Title = TITLE_FONT.render("Instructions", 1, colors.get("blue"))

    #fills screen with white
    screen.fill(colors.get("white"))

    #creating button options
    

    #Instructions
    myFile = open("PygameFiles\instructions.txt", "r")
    content = myFile.readlines()

    #var to controll change of line
    yinstructions = 150
    for line in content:
        Instruc = MENU_FONT.render(line[0:-1], 1, colors.get("blue"))
        screen.blit(Instruc, (40, yinstructions))
        pygame.display.update()
        pygame.time.delay(50)
        yinstructions += 40

    myFile.close()

    #renderig fonts to the screen
    xd = WIDTH//2 - (Title.get_width()//2)
    screen.blit(Title, (xd, 50))
    

    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                Mainmenu()         
def settings():
    global mx, my
    Title = TITLE_FONT.render("Settings", 1, colors.get("blue"))
    xd=WIDTH//2
    #fills screen with white
    screen.fill(colors.get("white"))
    ySettings=215
    mx=0
    my=0
    #creating button options
    Button_BG = pygame.Rect(xd, 200, WIDTH//3, 50)
    Button_Screen = pygame.Rect(xd, 300, WIDTH//3, 50)
    Button_Sound = pygame.Rect(xd, 400, WIDTH//3, 50)
    pygame.draw.rect(screen, colors.get("gold"), Button_BG)
    pygame.draw.rect(screen, colors.get("limeGreen"), Button_Screen)
    pygame.draw.rect(screen, colors.get("pink"), Button_Sound)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                mx = mousePos[0]
                my = mousePos[1]
                if Button_BG.collidepoint((mx, my)):
                    changeBG()
        for item in settingsList:
            text=MENU_FONT.render(item, 1, colors.get('blue'))
            screen.blit(text, (xd, ySettings))
            pygame.display.update()
            ySettings += 100
        #renderig fonts to the screen
        xd = WIDTH//2 - (Title.get_width()//2)
        screen.blit(Title, (xd, 100))
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    Mainmenu()

def changeBG():
    global screen, event, colors
    screen.fill(colors.get("white"))
    text = MENU_FONT.render("Below are your options for background colors. Pick the one you want, and then press the X to get back to the settings page.", 1, colors.get("blue"))
    screen.blit(text,(xd, 50))
    Button_pink = pygame.Rect(xd, 200, WIDTH//3, 50)
    Button_blue = pygame.Rect(xd, 300, WIDTH//3, 50)
    Button_limeGreen = pygame.Rect(xd, 400, WIDTH//3, 50)
    Button_white = pygame.Rect(xd, 400, WIDTH//3, 50)
    Button_gold = pygame.Rect(xd, 400, WIDTH//3, 50)
    pygame.draw.rect(screen, colors.get("pink"), Button_pink)
    pygame.draw.rect(screen, colors.get("blue"), Button_blue)
    pygame.draw.rect(screen, colors.get("limeGreen"), Button_limeGreen)
    pygame.draw.rect(screen, colors.get("white"), Button_white)
    pygame.draw.rect(screen, colors.get("gold"), Button_gold)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                mx = mousePos[0]
                my = mousePos[1]
                if Button_pink.collidepoint((mx, my)):
                    screen.fill(colors.get("pink"))
                    pygame.display.update()
                if Button_blue.collidepoint((mx, my)):
                    screen.fill(colors.get("blue"))
                    pygame.display.update()
                if Button_limeGreen.collidepoint((mx, my)):
                    screen.fill(colors.get("limeGreen"))
                    pygame.display.update()
                if Button_white.collidepoint((mx, my)):
                    screen.fill(colors.get("white"))
                    pygame.display.update()
                if Button_gold.collidepoint((mx, my)):
                    screen.fill(colors.get("gold"))
                    pygame.display.update()
                if event.type==pygame.QUIT:
                    settings()

    
def Game1():
    global bg,  cx, cy, mx, my, rad
    #images
    run=True
    bg=pygame.image.load('pygameFiles\imagesfolder\\bgSmaller.jpg')
    
    # screen.blit(bg, (0,0))
    # pygame.display.update()
    # pygame.time.delay(5000)
    while run:
        # screen.fill(backgrnd)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                print("Y quit")
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                mx = mousePos[0]
                my = mousePos[1]
        screen.blit(bg, (0,0))
        keys= pygame.key.get_pressed() #this is a list
        #mve square
        if keys[pygame.K_RIGHT] and square.x < WIDTH -(wb):
            square.x += speed
            
        if keys[pygame.K_LEFT] and  square.x > speed:
            square.x -= speed
            
        if keys[pygame.K_UP] and square.y >speed:   #means clser t 0
            square.y -= speed
            
        if keys[pygame.K_DOWN] and square.y <HEIGHT -hb:  #means clser t max value HEIGHT
            square.y += speed
            
            #mve Circle
        if keys[pygame.K_d] and cx < WIDTH -(rad):
            cx += speed
            
        if keys[pygame.K_a] and  cx > (speed+rad):
            cx -= speed
            
        if keys[pygame.K_w] and cy >(speed+rad):   #means clser t 0
            cy -= speed
            
        if keys[pygame.K_s] and cy <HEIGHT -(rad):  #means clser t max value HEIGHT
            cy += speed
         

        
        #rect(surface, color, rect) -> Rect
        pygame.draw.rect(screen, squareClr,square)
        #circle(surface, color, center, radius)
        pygame.draw.circle(screen, circleClr, (cx,cy), rad)
        pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                Mainmenu()
def Game2():

    global bg, char, charx, chary, insSquare, cx, cy, mx, my, rad
    #images
    run=True
    bg=pygame.image.load('pygameFiles\imagesfolder\\bgSmaller.jpg')
    char = pygame.image.load('PygameFiles\imagesfolder\PixelArtTutorial.png')
    char = pygame.transform.scale(char, (50, 50))
    # screen.blit(bg, (0,0))
    # pygame.display.update()
    # pygame.time.delay(5000)
    while run:
        # screen.fill(backgrnd)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                print("Y quit")
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                mx = mousePos[0]
                my = mousePos[1]
        screen.blit(bg, (0,0))
        keys= pygame.key.get_pressed() #this is a list
        #mve square
        if keys[pygame.K_RIGHT] and square.x < WIDTH -(wb):
            square.x += speed
            charx += speed
        if keys[pygame.K_LEFT] and  square.x > speed:
            square.x -= speed
            charx -= speed
        if keys[pygame.K_UP] and square.y >speed:   #means clser t 0
            square.y -= speed
            chary -= speed
        if keys[pygame.K_DOWN] and square.y <HEIGHT -hb:  #means clser t max value HEIGHT
            square.y += speed
            chary += speed
            #mve Circle
        if keys[pygame.K_d] and cx < WIDTH -(rad):
            cx += speed
            insSquare.x += speed
        if keys[pygame.K_a] and  cx > (speed+rad):
            cx -= speed
            insSquare.x -= speed
        if keys[pygame.K_w] and cy >(speed+rad):   #means clser t 0
            cy -= speed
            insSquare.y -= speed
        if keys[pygame.K_s] and cy <HEIGHT -(rad):  #means clser t max value HEIGHT
            cy += speed
            insSquare.y += speed

        if square.colliderect(insSquare):
            print("BOOM")
            rad+=1
            cx=random.randint(rad, WIDTH-rad)
            cy=random.randint(rad, HEIGHT-rad)
            ibox = rad*math.sqrt(2)
            xig = cx-(ibox/2)
            yig = cy-(ibox/2)
            insSquare=pygame.Rect(xig,yig,ibox,ibox)
        #rect(surface, color, rect) -> Rect
        pygame.draw.rect(screen, squareClr,square)
        screen.blit(char, (charx, chary))
        #circle(surface, color, center, radius)
        pygame.draw.circle(screen, circleClr, (cx,cy), rad)
        pygame.draw.rect(screen, squareClr, insSquare)
        pygame.display.update()
        clock.tick(150)
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                Mainmenu()           
                
def scoreboard():
    Title = TITLE_FONT.render("Scoreboard", 1, colors.get("blue"))

    #fills screen with white
    screen.fill(colors.get("white"))

    myFile = open("PygameFiles\scoreboard.txt", "r")
    content = myFile.readlines()

    #var to controll change of line
    yinstructions = 150
    for line in content:
        Instruc = MENU_FONT.render(line[0:-1], 1, colors.get("blue"))
        screen.blit(Instruc, (40, yinstructions))
        pygame.display.update()
        pygame.time.delay(50)
        yinstructions += 40

    myFile.close()

    #renderig fonts to the screen
    xd = WIDTH//2 - (Title.get_width()//2)
    screen.blit(Title, (xd, 50))

    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                Mainmenu()

name()
Mainmenu()

