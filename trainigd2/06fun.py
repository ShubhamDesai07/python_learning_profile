
for i in range (1,4):
    for j in range (i):
        print(i," ",end='')
    print() 



count = 1
for i in range (1,4):
    for j in range (1,i+1):
        print(count," ",end='')
        count=count+1
    print() 
