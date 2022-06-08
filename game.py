# Fernando Gupta
# create a word guess agme with 10 words
# pseudocode: provide instructions to user, one hint and the amount of words in the list, get guess. If correct congratulate. if not say you missed. if missed provide another hint. if correct congatulate if inncorect say, man wrong again and then provide third hint, if correct congatulate, if innocorect say you missed again, you are really bad at this, stop providing hits and give user unlimited guesses till correct 

from ctypes.wintypes import WORD
import random
import os 

os.system ('cls')
from time import sleep
seconds=.5



list1 = ["coral","scallop","sea urchin","oyster","mussel","cockle","clam","geoduck","abelone","ostrea"]
list2 = ["apple","banana","kiwi","strawberry","orange","cherry","blueberry","pear","peach","grape"]
list3 = ["basketball","hockey","rugby","football","soccer","lacrosse","swimming","golf","volleyball","boxing"]
Game=True
cnt=0
#a function is a section  the prram that we call when we need it
def hint():
    global cnt     #allow us to modify the variable all over the program
    if cnt ==0:
        print("|*************************************|")
        print("|         Here is a new hint          |")
        print("|These creatures all have a hard shell|")
        print("|        only 2 shells in fact        |")
        print("|*************************************|")
        

    # guess2 = input("plese put your new guess here: ")
    # if guess2 == theword:
    #     print("Congrats, You got it")
    # else:
    #     print("wrong again, you are pretty bad at this, try again")
    elif cnt ==1:     #else if
        print("|**************************************|")
        print("|       Here is your final hint        |")
        print("|  These creatures almost never move   |")
        print("|**************************************|")

    else:
        print("You are horrible at guessing, no more hints, go till you get it right")
        print()
def selectWord(choice):
    global theWord
    if choice==1:
        theWord=random.choice(list1)
    if choice==2:
        theWord=random.choice(list2)
    if choice==3:
        theWord=random.choice(list3)
    return theWord

while Game:
    theword=random.choice(list1)
    print("|***************************************|")
    print("|         Guessing  Game   !!           |")
    print("|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^|")
    print("|          1. animals                    |")
    print("|          2. fruits")
    print("|          3. sports    ")
    print("|First we will provide you with one hint|")
    print("|           !Your Hint Is!              |")
    print("|  These animals are big fans of water  |")
    print("|***************************************|")
# add user name, make it more personal y will need for keeping score
    name=input("What is your name? ")
    print(name, end=", ")
    answer=input("Would you like to play? ")
    if 'n' in answer:
        break
    while True:
        choice=input("What game would y like to play 1, 2, or 3")
        #preventing error we use try and except
        try:
            choice=int(choice)
            if choice>0 and choice <4:
                break
            else:
                print("give me 1,2  3")
        except:
            print("sorry")
    #call function to select the word from the right list
    os.system('cls')
    theWord=selectWord(choice)
    check=True
    while check and cnt <5:
        guess=input("plese put your guess here: ")
        print()
        if guess == theWord:
            print("Congrats, You got it")
        
            check=False
        else:
            hint()
        cnt+=1   # cnt= cnt + 1
        if cnt==5:
            print("sorry")
        score=200-40*cnt
        print(name+", your score is "+str(score))
        input("press enter")
    os.system('cls')
    print("<><><><><><><><><><><><>")
    answer=input("Do yo want to play again? ")
    if ('n' or 'N') in answer:
        Game=False
        print("Thank you for playing my game" )
cnt=0