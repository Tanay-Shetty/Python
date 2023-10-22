from threading import Thread
import threading
import time

class Buffer:
    def __init__(self,size):
        self.size=size
        self.b=[0]*size
        self.into=0
        self.out=0
        self.empty=threading.Semaphore(size)
        self.full=threading.Semaphore(0)
        self.mutex=threading.Semaphore(1)
    def getvalue(self):
        x=self.b[self.out]
        self.out=(self.out+1)%self.size
        return x
    def putvalue(self,value):
        self.b[self.into]=value
        self.into=(self.into+1)%self.size
    
class Producer(Thread):
    def __init__(self,buffer1):
        super(Producer,self).__init__()
        self.buffer1=buffer1
    def run(self):
        i=0
        while True:
            i+=1
            self.buffer1.empty.acquire()
            self.buffer1.mutex.acquire()
            self.buffer1.putvalue(i)
            self.buffer1.mutex.release()
            self.buffer1.full.release()
            print(f"Item {i} is put in buffer")
            time.sleep(5)

class Consumer(Thread):
    def __init__(self,buffer1):
        super(Consumer,self).__init__()
        self.buffer1=buffer1
    def run(self):
        while True:
            self.buffer1.full.acquire()
            self.buffer1.mutex.acquire()
            value=self.buffer1.getvalue()
            self.buffer1.mutex.release()
            self.buffer1.empty.release()
            print(f"Item {value} is consumed from buffer")
            time.sleep(5)
buffer1=Buffer(5)
p=Producer(buffer1)
q=Consumer(buffer1)
p.start()
q.start()
p.join()
q.join()
