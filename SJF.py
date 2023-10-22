finallist=[]
def getwt(n,plist):
    runtime=[0]*n
    for i in range(1,n):
        finallist.append(plist[0])
        prevbt=plist[0][2]
        plist.pop(0)
        runtime[i]=runtime[i-1]+prevbt
        plist=sorted(plist,key=lambda x:(x[2],x[1]))
        plist[0][3]=runtime[i]-plist[0][1]
    finallist.append(plist[0])

def gettat(n,plist):
    for i in range(n):
        plist[i][4]=plist[i][3]+plist[i][2]

def getavgtime(n,plist):
    getwt(n,plist)
    plist=finallist
    gettat(n,plist)
    print("Process\tBT\tAT\tWT\tTAT")
    totwt=0
    tottat=0
    for i in range(n):
        totwt+=plist[i][3]
        tottat+=plist[i][4]
        print(f"P{plist[i][0]}\t{plist[i][2]}\t{plist[i][1]}\t{plist[i][3]}\t{plist[i][4]}")
    avgwt=totwt/n
    avgtat=tottat/n
    print("Avgerage waiting Time ",avgwt)
    print("Avgerage TImeAround Time ",avgtat)

process_list=[]
n=int(input("Enter the number of process: "))
for i in range(n):
    process=list(map(int,input("Enter the process no,arrival time,burst time separated by space").split()))
    process.extend([0,0])
    process_list.append(process)
process_list=sorted(process_list,key=lambda x:(x[1],x[2]))
print(process_list)
getavgtime(n,process_list)