#Eitan Hahn
#Guess a word in a list
import os
os.system('cls')
import random

for i in range(19):
    print("-",end="")
print()
print('| Guess the word! |')
for i in range(19):
    print("-",end="")
print()
print('|Guess the correct|')
print('|  animal to win  |')

for i in range(19):
    print("-",end = "")
print()
thislist = ["giraffe", "deer","horse", "sheep", "squirrel", "dog","lion","cat","bear","pig" ]
print()
for i in range(54):
    print("*",end="")
print()
print('Instructions:')
print('1. A random word will be selected from a list of animals')
print('2. try to guess which animal was selected') 
for i in range(54):
    print("*",end="")
print()
print('got it? get ready!')
for i in range(28):
    print("*",end="")
print()
word=random.choice(thislist) #picks a random element in the list
print('hint: the animal is a mammal')
print()
guess=input("guess the animal:")
print()
if guess in word:
    print('congratulations! you guessed the correct word')
else: 
    print('sorry, you missed')