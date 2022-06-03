#Eitan Hahn
#Integers and float homework
#is number inputed by user even or odd
#is number a multiple of 3 or 5
from ast import Num
import os
os.system('cls')
variable=input('enter a number') #asking for user's number
num=int(variable) #making sure number is integer
variable=(num%2)
print(num % 2) #using modulus to get the remainder of the number divided by 2
if variable == 0:
    print('your number is even')
else:
    print('your number is odd')
#is number a multiple of 3?

