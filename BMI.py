#Eitan Hahn
#Calculate BMI
#get user weight and height
import os
os.system('cls')
#use variables
kg= 70
m= 2
weight= kg #this is a number
#weight=#input('how much you weight, ') give us a string
weight= int(input('how much you weight, ')) #typecast
height = m #this is a number
#height=#input('how tall you are, ') give us a string
height= int(input('how tall you are, ')) #typecast
BMI = weight / (height*height) 
#operators *,/
print ('your BMI is', BMI) 