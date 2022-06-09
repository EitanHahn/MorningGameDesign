#Eitan Hahn
#Learning about files
#r read
#w write
#a append
#
#open files and make sure to close files

import os, datetime
os.system('cls')
name="eitan"
score=120
date=datetime.datetime.now() #today's date and time

scoreLine= str(score) + "\t" + name + "\t" + (date.strftime("%m/%d/%y"))
print(scoreLine)

#to open a file we must create an object
myFile=open("score.txt",'w') #open a file to write. it will clear the file if it exists
myFile.write(scoreLine)
myFile.close()
myFile=open("score.txt",'a')
myFile.write(scoreLine)
myFile.close()
myFile=open("score.txt",'r') #open file to read
#lines=myFile.readlines
print()
for line in myFile.readlines():
    print(line)
myFile.close()