#Eitan Hahn
#We are going to learn about strings '' or ""
import os
os.system('cls')
print('Hi')
print("Hi")
print("Hi, let's go to the park")
message="you are awesome"#A string is an array characters
#      0   1   2   3   4   5 #all ararys begin in zero
#      H    E   L   L   O
print(message)
print(message[5]) #print the letter in position 5
print (message[0:5]) #print all letter from position 0 to 4 5 characters
if message.isdigit(): #isdigit is a method you must use with a dot
    sum=message +3 #if the statement is true 
else:              #if it is false
    print(message+"if i say so") #concatenation
print(message.upper())
print(message)
message=message.upper()
print(message)
if message.isupper():
    print(message)
else:
    #print("i am in false") #only use for debugging I will delete or com when I am done
    message=message.upper()
    print(message)
print(type(message))
print(dir(message)) #list of all methods

