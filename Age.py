# Eitan Hahn
# Calculate age
# get user year and current year
import os 
os.system('cls')
by= 2006 #this is a number
#by= #input('year you were born, ') give us a string
by = int(input('year you were born, ')) #typecast
currentYear=2022 #alsa number
age=currentYear-by
print ('Your age is', age)
#selection
if age >50:
    print('You are old')
