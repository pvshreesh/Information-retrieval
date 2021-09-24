import lsh
import numpy

f = open('dataset.txt', encoding='utf-8')
fopen = f.readlines()
print(len(fopen))
f.close()
def frint():
    resultset=lsh.setGenerator()
    for i in resultset:
        if i[0]==0 :
            print(i)
            print(fopen[i[1]])
        elif i[1]==0:
            print(i)
            print(fopen[i[0]])

frint()
with open("dataset.txt") as f: 
    lines = f.readlines() #read 

    #modify 
lines=lines[1:]  
 
with open("dataset.txt", "w") as f: 
    f.writelines(lines)  
