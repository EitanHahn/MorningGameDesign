#Eitan Hahn
#We are going to learn about lists, functions to lists
#We are going to learn about forloop
import os
import random
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

for num in range(10): #loops a specific number of times
    print(num,end= " ")

print()

for element in thislist: #element = thislist (times run through loop)
    print(element,end= " ")

thislist.append("pinapple") #add an element to the end of the list
print(thislist[0:])

#for num in range(2):
    #thislist.append(input("input a food"))
#print(thislist[0:])

thislist.insert(1,"pinapple") #adding an element to a specific index insert (index, element you want to add)
print(thislist[0:])

for i in range(len(thislist)):
    print(thislist[i], end=" / ")
print()

list_num = [1, 2, 3, 4]
list_num.extend(thislist) #adds the elements
print(list_num)

list_num = [1, 2, 3, 4]
list_num.append(thislist) #adds the whole list to the last index
print(list_num[-1]) #print the last element
print(list_num[-1][0]) #print an element in in an element if that element is a list [0,1,2,3,]

word=random.choice(thislist) #picks a random element in the list
print(word)

guess=input("input a food")
if guess in word:
    print("congrats, you guessed the word")