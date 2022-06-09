#Eitan Hahn
#Guess the number game
import os

os.system('cls')
import random
cnt=0
name=input('What is your name? ')
print(name,end="")
print(', welcome to the guess the number game.')
print('you will have 6 options on the main menu. choose one.')
print('---------------------')
print('GUESS THE NUMBER GAME')
print('---------------------')
print('1. Instructions')
print('2. Level 1: 1-25')
print('3. Level 2: 1-50')
print('4. Level 3: 1-100')
print('5. Scoreboard')
print('6. Exit game')
print()
choice=int(input('input the which option you would like to go to.' ))


print (name, end="" )
theNum=0
Game=True
level=""
def selectNum(choice):
    global theNum, level
    if choice==1:
        myFile=open('Instructions.txt''r') 
        for line in myFile.readlines():
            print(line)
        myFile.close()
    if choice==2:
        theNum=random.randint(1,25)  # you must give a beginning and end
        level="1-25"
    if choice==3:
        theNum=random.randint(1,50)
        level="1-50"
    if choice==4:
        theNum=random.randint(1,100) 
        level="1-100"
    if choice==5:
        myFile=open('scores.txt''r')
    return theNum
    
while Game:
    theNum=selectNum(choice)
    

    check=True
    while check and cnt < 20:
        try:
            message="guess a number between "+ level
            guess=int(input(message))
            if guess == theNum:
                print('congratulations! you guessed the correct number')
            else:
                print("sorry, you didn't guess the right number. try to guess again")
        except:
            print('give me a number between '+ level)
            cnt+=1
            if cnt==20:
                print('sorry, you ran out of guesses')
            score=200-40*cnt
            print(name,'your score is'+str(score))
            input=('press enter to go back to menu')
            cnt+=1





