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
            print("Stack Overflow")
        else:
            self.top += 1
            self.items[self.top] = data

    def pop(self):
        if self.is_empty():
           print("Stack Underflow")
        else:
            del self.items[self.top]
            self.top -=1

    def status(self):
       
        while True:
        
            c = int(input("1)Push\n2)pop\n3)Exit\nEnter your choice: "))
        
            if c == 1:
                d = input("Enter the data to push: ")
                self.items.append(d)
            elif c== 2:
                self.items.pop()
            elif c== 3:
                break
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
