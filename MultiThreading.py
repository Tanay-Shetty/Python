import threading

def prime(n1,n2):
    print("The current thread running is ",threading.current_thread().name)
    p=[]
    for i in range(n1,n2+1):
        if(i==1):
            continue
        for j in range(2,i):
            if(i%j==0):
                break
        else:
            p.append(i)
    print("The prime number from",n1," to ",n2," is:",p)
t1=threading.Thread(target=prime,args=(1,20),name="t1")
t2=threading.Thread(target=prime,args=(1,100),name="t2")
t1.start()
t2.start()
t1.join()
t2.join()
print("All the thread are executed")