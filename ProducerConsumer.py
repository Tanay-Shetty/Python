from collections.abc import *
from threading import Thread
import time
from typing import *

class Buffer:
    def __init__(self,size):
        self.size=size
        self.b=[0]*size
        self.into=0
        self.out=0
        self.counter=0
    def getValue(self):
        x=self.b[self.out]
        self.out=(self.out+1)%self.size
        self.counter-=1
    def putValue(self,value):
        self.b[self.into]=value
        self.into=(self.into+1)%self.size
        self.counter+=1

class Producer(Thread):
    def __init__(self,buffer1):
        super(Producer,self).__init__()
        self.buffer1=buffer1
    def run(self):
        i=0
        while self.buffer1.counter<self.buffer1.size:
            i+=1
            self.buffer1.putValue(i)
            print(f"Item {i} is put in buffer \n Current ItemCount:{self.buffer1.counter}")
            time.sleep(5)

class Consumer(Thread):
    def __init__(self,buffer1):
        super(Consumer,self).__init__()
        self.buffer1=buffer1
    def run(self):
        while self.buffer1.counter!=0:
            value=self.buffer1.getValue()
            print(f"Item {value} is put in buffer \n Current ItemCount:{self.buffer1.counter}")
            time.sleep(5)
buffer1=Buffer(5)
p=Producer(buffer1)
q=Consumer(buffer1)
p.start()
q.start()
p.join()
q.join()
