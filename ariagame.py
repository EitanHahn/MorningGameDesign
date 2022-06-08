import random
import os 
os.system('cls')

for i in range (75): #this is for title screen
            print("*", end="")
print("  ")
name=input("what is your name? ")
print("     ")
print()
print(name, end=", ")
print()
print("hello! welcome to the guessing game!")
print("you will have five guesses to figure out a specific word")
print("good luck!")
print("     ")

Game=True 
def option1():
    os.system('cls')
    check = True
    count = 0
    list = ["ariana grande", "taylor swift", "harry styles", "lorde", "dua lipa", "olivia rodrigo", "billie eilish", "ed sheeran", "katy perry", "doja cat" ]
    theword=random.choice(list)
    while check and count <5:
        guess=input("please put your guess for singer here: ")
        if guess.lower() == theword.lower():
            print("Congrats, You got it")
            print(" |      |")
            print("[|      |]")
            print(" \      /")
            print("   \  /")
            print("    ||")
            print("    --")
            input("press enter when done")
    
            check = False
        count += 1
def option2():
    os.system('cls')
    check = True
    count = 0
    list = ["banana", "pineapple", "apple", "pear", "orange", "mango", "papaya", "blueberry", "kiwi", "strawberry" ]
    theword=random.choice(list)
    while check and count <5:
        guess=input("please put your guess for fruit here: ")
        if guess.lower() == theword.lower():
            print("Congrats, You got it")
            print(" |      |")
            print("[|      |]")
            print(" \      /")
            print("   \  /")
            print("    ||")
            print("    --")
            input("press enter when done")

            check = False
        count += 1
def option3():
    os.system('cls')
    check = True
    count = 0
    list = ["dog, cat, panda, pig, hippo, penguin, turtle, giraffe, tiger, lion" ]
    theword=random.choice(list)
    while check and count <5:
        guess=input("please put your guess for animal here: ")
        if guess.lower() == theword.lower():
            print("Congrats, You got it")
            print(" |      |")
            print("[|      |]")
            print(" \      /")
            print("   \  /")
            print("    ||")
            print("    --")
            input("press enter when done")
    
            check = False
        count += 1

   
while Game:
    print("1. guess the singer")
    print("2. guess the fruit")
    print("3. guess the animal")
    

    print() 
    while True:
        choice=input("what game would you like to play? 1, 2, or 3?: ")
        try:
            choice=int(choice)
            if choice >0 and choice <4:
                break
            else:
                print("give me 1, 2, or 3 please!")
        except:
            print("sorry")
    

    os.system('cls')
    if choice==1: 
        option1()
    if choice==2:
        option2()
    if choice==3:
        option3()

    os.system('cls')
    answer=input("would you like to play again? " )
    if ('n' or 'N') in answer:
        Game=False 