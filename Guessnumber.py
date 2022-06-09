#Eitan Hahn
#Guess the number game
import os

os.system('cls')
import random
cnt=0
print('---------------------')
print('GUESS THE NUMBER GAME')
print('---------------------')
print('Level 1: 1-25')
print('Level 2: 1-50')
print('Level 3: 1-100')
print()
name=input('What is your name? ')
print (name, end="" )
Game=True
level=""
theNum=0
def selectNum(choice):
    global theNum, level
    if choice==1:
        theNum=random.randint(1,25)  # you must give a beginning and end
        level="1-25"
    if choice==2:
        theNum=random.randint(1,50)
        level="1-50"
    if choice==3:
        theNum=random.randint(1,100) 
        level="1-100"
    return theNum
    
while Game:
    choice=input(', which level would you like to play? ')
    
    while True:         # the try and except should be in a while loop
        try:
            choice=int(choice) 
            if choice > 0 and choice < 4:
                break
            else:
                print('give me 1, 2, or 3')
        except:
            print('Tell me which level you want to play')
        print(choice)
    theNum=selectNum(choice)
    print(theNum)

    check=True
    while check and cnt < 5:
        
        message="guess a number between "+ level
        guess=input(message)
        if guess is theNum:
            print('congratulations! you guessed the correct number')
            check = False
        else:
            print("sorry, you didn't guess the right number")





