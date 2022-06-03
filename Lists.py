#Eitan Hahn
#We are going to learn about lists, functions to lists
#We are going to learn about forloop
import os
os.system('cls')

thislist = ["apple", "banana", "cherry","orange","kiwi","melon","mango"]
#              0         1         2        3       4      5       6
#                                 -5       -4      -3     -2      -1      
print(thislist[1]) #print from specific index
print(thislist[-1]) #print from the end
print(thislist[2:5]) #print from two value the first one is included
print(thislist[:3]) #print up to a value but not including a value
print(thislist[2:]) #print everything after a value including the original element
print(thislist[-4:-1])


if "apple" in thislist:
    print ("yes, the apple is in the list")

for num in range(10):
    print(num,end= " ")

print()

for element in thislist: #element = thislist (times run through loop)
    print(element,end= " ")

thislist.append("pinapple") #add an element to the end of the list
print(thislist[0:])