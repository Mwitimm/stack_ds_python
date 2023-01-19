from random import random
from  math import floor
#implementing stack with an array
class MyStack:
    stack = []
    top = -1
    size = 0
    def __init__(self,size):
        self.size = size
        #return self.size
    def isfull(self):
        return self.top == self.size-1
    def isempty(self):
        return self.top == -1
    
    def push(self,n):
        if self.isfull():
            print("Sorry the stack is full")
        else:
            self.top+=1
            self.stack.append(n)
            print(f"Pushed {n}")
    def stackPop(self):
        if self.isempty():
             print("Sorry the stack is empty")
        else:
            print(f"removed {self.stack[self.top]}")
            self.top -= 1 
            return self.stack[:-1]      
            
#create a stack object of size 10
stack = MyStack(10)
add = 0
remove = 0
while add <= 10:
    #generate random random numbers between 0 and 100 and push them to a stack
    item = floor((random())*100)
    stack.push(item)
    add += 1          
while remove <=10:
    stack.stackPop()
    remove += 1
