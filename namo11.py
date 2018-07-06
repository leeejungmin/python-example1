import random

cT=[[0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]]

for i in range(5):
    for j in range(5):
        cT[i][j]=random.randint(0,1)

aT=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

dT=[[0,0,0],
    [0,0,0],
    [0,0,0],
    [0,0,0],
    [0,0,0]]

bT=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

count=0
num=0
for i in range(5):
    
    
    for j in range(5):
        if cT[i][j]==1:
            count=count+1
        elif cT[i][j]==0:
            aT[num]=count
            count=0
        if 0<=j and j<=3:
            if cT[i][j+1]!=0:
                num=num+1



            
        if j==4:
            aT[num]=count
            num=num+1    
            count=0
           
j=0
for i in range(len(aT)):
    if aT[i] != 0:
        
        bT[j]=aT[i]
        j=j+1
    

print(cT)
print(aT)
print(bT)
               
