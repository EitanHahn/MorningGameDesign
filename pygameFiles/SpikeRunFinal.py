#Eitan Hahn
#6/24/22
#Final Game
import pygame, time,os,random, math, datetime,sys
pygame.init()#initialize the pygame package
date=datetime.datetime.now()
os.system('cls')
WIDTH=900 #like constant
HEIGHT=600
TITLE_FONT = pygame.font.SysFont('comicsans', WIDTH//20)
MENU_FONT = pygame.font.SysFont('comicsans', WIDTH//25)
INSTRUC_FONT = pygame.font.SysFont('comicsans', WIDTH//50)
colors={"white":(255,255,255),"pink":(255,0,255),"blue":(0,0,255),"limeGreen":(153,255,51),"gold":(255,215,0)}
clr=colors.get("limeGreen")
menuColor = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

message=["Instructions", "Settings", "Level 1", "Level 2", "Scoreboard", "Exit"]
settingsList=["Random Background color","Screen Size UP 100","Screen Size DOWN 100"]
#create dispay wind with any name y like
screen=pygame.display.set_mode((WIDTH,HEIGHT)) 
pygame.display.set_caption("Spike Run Game")  #change the title of my window


clock=pygame.time.Clock()

#mouse varuables
mx = 0
my = 0
score=0


run = True
Game = False
xd=WIDTH//2
def name():
    global user_name
    screen.fill(menuColor)
    run=True #to run the while loop
    user_name=''
    nameClr=(0,105,105) #for the text of the name
    boxClr= (200,200,200) #for the text box
    title=TITLE_FONT.render("Enter Name",1,boxClr)
    screen.blit(title,(WIDTH//2.75,HEIGHT//3.2)) 
    input_rect = pygame.Rect((WIDTH//2.4, HEIGHT//2.2), (140, 40))

    #make box
    while run:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                #Menu(mainTitle,messageMenu)
                Mainmenu()
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_RETURN: #if enter is pressed
                    #run main menu
                    Mainmenu()
                if event.key==pygame.K_BACKSPACE: #deleting characters
                    user_name=user_name[:-1]
                else:
                    user_name+=event.unicode
            pygame.draw.rect(screen, boxClr, input_rect)
            
            text_surface = MENU_FONT.render(user_name, True, nameClr)
            #use your x,y
            screen.blit(text_surface,(input_rect.x,input_rect.y-5))

            pygame.display.flip()
            clock.tick(60)

def Mainmenu():
    global xd, WIDTH, HEIGHT
    xd = WIDTH//2.5
    Title = TITLE_FONT.render("Spike Run", 1, colors.get("blue"))
    screen.fill(menuColor)
    screen.blit(Title, (WIDTH//2.5, 50))
    yMenu=155
    ByeBye = TITLE_FONT.render("ByeBye", 1, colors.get("blue"))
    Button_Instructions= pygame.Rect((xd, 160), (WIDTH//4, 40))
    Button_Settings = pygame.Rect((xd, 210 ), (WIDTH//4, 40))
    Button_Game1 = pygame.Rect((xd, 260), (WIDTH//4, 40))
    Button_Game2 = pygame.Rect((xd, 310), (WIDTH//4, 40))
    Button_Scoreboard = pygame.Rect((xd, 360), (WIDTH//4, 40))
    Button_Exit = pygame.Rect((xd, 410), (WIDTH//4, 40))
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
                    pygame.quit()
                    sys.exit()

def Instructions():
    #rendering text objects
    Title = TITLE_FONT.render("Instructions", 1, colors.get("blue"))

    #fills screen with white
    screen.fill(menuColor)

    #creating button options
    

    #Instructions
    myFile = open("PygameFiles\instructions.txt", "r")
    content = myFile.readlines()

    #var to controll change of line
    yinstructions = 90
    for line in content:
        Instruc = INSTRUC_FONT.render(line[0:-1], 1, colors.get("blue"))
        screen.blit(Instruc, (40, yinstructions))
        pygame.display.update()
        pygame.time.delay(50)
        yinstructions += 30

    myFile.close()

    #renderig fonts to the screen
    xd = WIDTH//2 - (Title.get_width()//2)
    screen.blit(Title, (xd, 25))
    

    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                Mainmenu()         
def settings():
    global menuColor, WIDTH, HEIGHT, screen
    xd=WIDTH//3.5
    Title = TITLE_FONT.render("Settings", 1, colors.get("blue"))
    
    #fills screen with the menu color
    screen.fill(menuColor)
    ySettings=215
    mx=0
    my=0
    #creating button options
    Button_BG = pygame.Rect(xd, 210, WIDTH//2, 50)
    Button_ScreenUp = pygame.Rect(xd, 310, WIDTH//2, 50)
    Button_ScreenDown = pygame.Rect(xd, 410, WIDTH//2, 50)

    #drawing buttons
    pygame.draw.rect(screen, colors.get("gold"), Button_BG)
    pygame.draw.rect(screen, colors.get("limeGreen"), Button_ScreenUp)
    pygame.draw.rect(screen, colors.get("pink"), Button_ScreenDown)
    for item in settingsList:
        text=MENU_FONT.render(item, 1, colors.get('blue'))
        screen.blit(text, (xd, ySettings))
        pygame.display.update()
        ySettings += 100
    #renderig fonts to the screen
    screen.blit(Title, (WIDTH//2.5, 100))

    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                Mainmenu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                mx = mousePos[0]
                my = mousePos[1]
                if Button_BG.collidepoint((mx, my)):
                    menuColor = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
                    pygame.display.update()
                    Mainmenu()
                if Button_ScreenUp.collidepoint((mx,my)) and WIDTH <1000 and HEIGHT<1000:
                    WIDTH +=100
                    HEIGHT +=100
                    screen=pygame.display.set_mode((WIDTH, HEIGHT))
                    Mainmenu()
                if Button_ScreenDown.collidepoint((mx,my)) and WIDTH>600 and HEIGHT>600:
                    WIDTH -=100
                    HEIGHT -=100
                    screen=pygame.display.set_mode((WIDTH, HEIGHT))
                    Mainmenu()  
def Game1():
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
    platform1_rect=pygame.Rect(100,220, 100, 50)
    platform2_rect=pygame.Rect(315,400, 100, 50)
    platform3_rect=pygame.Rect(490,250, 100, 50)
    platform5_rect=pygame.Rect(660,400, 100, 50)
    hitbox=pygame.Rect(x+5,y+10,40,40) #figure out dimension of character
    coin1_rect=pygame.Rect(130,400,45,45)
    coin2_rect=pygame.Rect(340,250,45,45)
    coin3_rect=pygame.Rect(500,400,45,45)
    coin4_rect=pygame.Rect(690,200,45,45)
    treasure_rect=pygame.Rect(795,375,100,80)
    #blitting the background, platforms, and coins to the level
    def redrawwindow():
        global walkCount, x, y
        screen.blit(bg, (0,0))  #background at 0,0
        screen.blit(platform1,(100,220))
        screen.blit(platform1,(315,400))
        screen.blit(platform1,(490,250))
        screen.blit(platform1,(660,400))
        screen.blit(coin1,(130,400))
        screen.blit(coin2,(340,250))
        screen.blit(coin3,(500,400))
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
            if event.type == pygame.QUIT: #if press on X, run menu
                Mainmenu()
            
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
            y=240
            hitbox.x= x+5
            hitbox.y= y
        if platform2_rect.colliderect(hitbox):
            x=0
            y=395
            hitbox.x= x+5
            hitbox.y= y
        if platform3_rect.colliderect(hitbox):
            x=0
            y=265
            hitbox.x= x+5
            hitbox.y= y
        if platform5_rect.colliderect(hitbox):
            x=0
            y=395
            hitbox.x= x+5
            hitbox.y= y
        if hitbox.colliderect(treasure_rect):
            endGameL1()


        if coin1_rect.colliderect(hitbox):
            coin1 = pygame.Surface((24, 24), flags=pygame.SRCALPHA)
            coin1.fill((0, 0, 0, 0)) #RGBA sequence
            coin1_rect=pygame.Rect(0,0,40,40)
            score+=1
        if coin2_rect.colliderect(hitbox):
            coin2 = pygame.Surface((24, 24), flags=pygame.SRCALPHA)
            coin2.fill((0, 0, 0, 0)) #RGBA sequence
            coin2_rect=pygame.Rect(0,0,40,40)
            score+=1
        if coin3_rect.colliderect(hitbox):
            coin3 = pygame.Surface((24, 24), flags=pygame.SRCALPHA)
            coin3.fill((0, 0, 0, 0)) #RGBA sequence
            coin3_rect=pygame.Rect(0,0,40,40)
            score+=1
        if coin4_rect.colliderect(hitbox):
            coin4 = pygame.Surface((24, 24), flags=pygame.SRCALPHA)
            coin4.fill((0, 0, 0, 0)) #RGBA sequence
            coin4_rect=pygame.Rect(0,0,40,40)
            score+=1

        redrawwindow()
        #creating time
        if current_time - button_press_time > 20000: #if the time reaches 20 seconds, run the endgame function
            noTimeL1()
def noTimeL1(): #function if game reaches time limit
    screen.fill(menuColor)
    text2= TITLE_FONT.render("You ran out of Time!", 1, colors.get("blue"))
    screen.blit(text2,(240,250))
    pygame.display.update()
    pygame.time.delay(1000)
    Mainmenu()
def endGameL1(): #function for if character reaches treasure
    screen.fill(menuColor)
    text2= MENU_FONT.render("Congratulations! You reached the Treasure", 1, colors.get("blue"))
    scoretext=MENU_FONT.render('Your score is '+str(score), 1, colors.get('blue'))
    screen.blit(scoretext, (WIDTH/3, HEIGHT/1.75))
    screen.blit(text2,(100,200))
    pygame.display.update()
    pygame.time.delay(1750)
    Mainmenu()
def Game2():
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
            if event.type == pygame.QUIT: #if press on X, run menu
                Mainmenu()
            
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
            
        if coin2_rect.colliderect(hitbox):
            coin2 = pygame.Surface((24, 24), flags=pygame.SRCALPHA)
            coin2.fill((0, 0, 0, 0)) #RGBA sequence
            coin2_rect=pygame.Rect(0,0,40,40)
            score+=1
            
        if coin3_rect.colliderect(hitbox):
            coin3 = pygame.Surface((24, 24), flags=pygame.SRCALPHA)
            coin3.fill((0, 0, 0, 0)) #RGBA sequence
            coin3_rect=pygame.Rect(0,0,40,40)
            score+=1
           
        if coin4_rect.colliderect(hitbox):
            coin4 = pygame.Surface((24, 24), flags=pygame.SRCALPHA)
            coin4.fill((0, 0, 0, 0)) #RGBA sequence
            coin4_rect=pygame.Rect(0,0,40,40)
            score+=1

        redrawwindow()
        if current_time - button_press_time > 20000: #if the time reaches 20 seconds, run the endgame function
            noTimeL2()
def noTimeL2(): #function if game reaches time limit
    screen.fill(colors.get("white"))
    text2= TITLE_FONT.render("You ran out of Time!!", 1, colors.get("blue"))
    screen.blit(text2,(240,250))
    pygame.display.update()
    pygame.time.delay(1000)
    Mainmenu()
def endGameL2():
    screen.fill(menuColor)
    text2= MENU_FONT.render("Congratulations! You reached the Treasure", 1, colors.get("blue"))
    scoretext=MENU_FONT.render('Your score is '+str(score), 1, colors.get('blue'))
    screen.blit(scoretext, (WIDTH/3, HEIGHT/1.75))
    screen.blit(text2,(100,250))
    pygame.display.update()
    pygame.time.delay(1750)
    Mainmenu() 
                
def scoreboard():
    
    Title = TITLE_FONT.render("Scoreboard",1, colors.get("blue")) #title of screen
    
    #fills screen with bg color
    screen.fill(menuColor)

    #open score file and write the score line in it
    scrLine="score: "+str(score)+"     "+ user_name+"     "+ date.strftime("%m-%d-%Y")
    myFile = open("pygameFiles\spikerunScoreboard.txt", "a")
    myFile.write(str(scrLine))
    myFile.close()

    #read score file
    myFile=open('pygameFiles\spikerunScoreboard.txt', 'r')
    content = myFile.readlines()

    #variable to control change of line
    yscore = 150
    for line in content:
        scores = MENU_FONT.render(line[0:-1], 1, colors.get("blue"))
        screen.blit(scores, (40, yscore))
        pygame.display.update()
        pygame.time.delay(25)
        yscore += 40
    myFile.close()

    #back to menu if quit
    scoreboard=True
    while scoreboard:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                Mainmenu()
    screen.blit(Title,(WIDTH//3,50))




 

name()
Mainmenu()

