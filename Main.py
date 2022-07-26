import os
class Stack:
    def __init__(self, size):
        self.items = []
        self.size = size
        self.top = -1

    def is_empty(self):
        
        return self.top == -1
    def is_full(self):
       return self.top == self.size-1
    def push(self, data):
        if self.is_full():
            return
        else:
            self.top += 1
            self.items.append(data)

    def pop(self):
        if self.is_empty():
           return
        else:
            del self.items[self.top]
            self.top -=1

    def status():
        size = int(input())
        queries = int(input())
        on = Stack(size)
        for t in range(queries):
        
            c = int(input())
        
            if c == 1:
                d = input()
                ob.items.append(d)
            elif c== 2:
                ob.items.pop()
         #print(ob.items)     
# Do not change the following code
size, queries = map(int, input().rstrip().split())
stack = Stack(size)
for line in range(queries):
    values = list(map(int, input().rstrip().split()))
    if values[0] == 1:
        stack.push(values[1])
    elif values[0] == 2:
        stack.pop()
stack.status()
