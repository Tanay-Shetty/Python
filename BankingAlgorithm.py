n=int(input("Enter number of process"))
m=int(input("Enter number of resources"))
Allocation=[]
Max=[]
Need=[]
Available=[]
Resource=[]
print("Enter the allocation matrix elements(one line at a time):")
for i in range(n):
    rowinput=[]
    for j in range(m):
        x=int(input())
        rowinput.append(x)
    Allocation.append(rowinput)
print("Enter the Max matrix elements(one line at a time):")
for i in range(n):
    rowinput=[]
    for j in range(m):
        x=int(input())
        rowinput.append(x)
    Max.append(rowinput)
for i in range(n):
    rowinput=[]
    for j in range(m):
        x=Max[i][j]-Allocation[i][j]
        rowinput.append(x)
    Need.append(rowinput)
for i in range(m):
    x=int(input("Enter the instances: "))
    Resource.append(x)
for j in range(m):
    x=0
    for i in range(n):
        x+=Allocation[i][j]
    y=Resource[j]-x
    Available.append(y)


work=Available.copy()
finish=[0]*n
Sequence=[]
alldone=False
attempt=0
while alldone==False:
    attempt+=1
    for i in range(n):
        if(finish[i]==0 and Need[i]<=work):
            for k in range(m):
                work[k]+=Allocation[i][k]
            finish[i]=1
            Sequence.append(i)
    for i in range(n):
        if finish[i]==0:
            break
    else:
        alldone=True
    if(attempt>2):
        break
    if(alldone==True):
        print("System is in safe state")
        print("safe sequence is ",Sequence)
    else:
        print("System is not in safe state")