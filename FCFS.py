def getwaitingtime(n,bt,at,wt):
    st=[0]*n
    for i in range(1,n):
        st[i]=st[i-1]+bt[i-1]
        wt[i]=st[i]-at[i]
def getturnaroundtime(n,bt,wt,tt):
    for i in range(n):
        tt[i]=wt[i]+bt[i]

def display(n,pid,bt,at):
    wt=[0]*n
    tt=[0]*n
    getwaitingtime(n,bt,at,wt)
    getturnaroundtime(n,bt,wt,tt)
    totwt=0
    tottt=0
    print(f"ProcessId\tBT\tAT\tWT\tTAT")
    for  i in range(n):
        totwt+=wt[i]
        tottt+=tt[i]
        print(f"P{pid[i]}\t\t{bt[i]}\t{at[i]}\t{wt[i]}\t{tt[i]}")
    avgwt=totwt/n
    avgtat=tottt/n
    print("The Average Waiting Time is:",avgwt)
    print("The Average TurnAround Time is:",avgtat)
    
n=int(input("ENter the no.of Process: "))
proc=list(map(int,input("Enter the processid seperated by space ").split()))
burst=list(map(int,input("Enter the BurstTime seperated by space ").split()))
arrival=list(map(int,input("Enter the ArrivalTime seperated by space ").split()))
display(n,proc,burst,arrival)

def getwaitingtime(n,bt,at,wt):
    starttime=[0]*n
    for i in range(1,n):
        starttime[i]=starttime[i-1]+bt[i-1]
        wt[i]=starttime[i]-at[i]
def getturnaroundtime(n,bt,wt,tt):
    for i in range(n):
        tt[i]=wt[i]+bt[i]


 

# def display(n,pid,bt,at):
#     wt=[0]*n
#     tt=[0]*n
#     getwaitingtime(n,bt,at,wt)
#     getturnaroundtime(n,bt,wt,tt)
#     totwt=0
#     tottt=0
#     print("ProcessID\tBT\tAT\tWT\tTAT")
#     for i in range(n):
#         totwt+=wt[i]
#         tottt+=tt[i]
#         print(f"\tP{i}\t{bt[i]}\t{at[i]}\t{wt[i]}\t{tt[i]}")
#     avgwt=totwt/n
#     avgtt=tottt/n
#     print(f"Average Waiting-Time ==> {round(avgwt,2)} && Average TurnAround-Time ==> {round(avgtt,2)}")

 

# n=int(input("Enter no of process: "))
# processes=list(map(int,input("Enter process ids seperated by space").split()))
# burstTime=list(map(int,input("Enter burst time seperated by space").split()))
# arrivalTime=list(map(int,input("Enter arrival time seperated by space").split()))
# display(n,processes,burstTime,arrivalTime)