'''
BOJ 10828 스택
https://www.acmicpc.net/problem/10828

stack class 구현
'''

import sys

class Stack:
    def __init__(self):
        self.stack = []

    def __getitem__(self, idx):
        return self.stack.__getitem__(idx)

    def action(self, order, num=None):
        if order == 'push':
            self.push(num)

        elif order == 'pop':
            self.pop()

        elif order == 'size':
            self.size()
        
        elif order == 'empty':
            self.empty()
        
        elif order == 'top':
            self.top()

    def push(self, num):
        self.stack.append(num)
    
    def pop(self):
        try:
            print(self.stack.pop())
        except IndexError:
            print(-1)
    
    def size(self):
        print(len(self.stack))

    def empty(self):
        if self.__is_empty():
            print(1)
        else:
            print(0)
    
    def __is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def top(self):
        if self.__is_empty():
            print(-1)
        else:
            print(self.stack[-1])


import sys

n = int(sys.stdin.readline())
stack = []

for i in range(n):
    temp = sys.stdin.readline().rstrip()
    
    if len(temp.split()) != 1:
        order, num = temp.split()
        num = int(num)
    else:
        order = temp
    
    if order == 'push':
        stack.append(num)
        
    elif order == 'pop':
        try:
            print(stack.pop())
        except IndexError:
            print(-1)

    elif order == 'size':
        print(len(stack))
    
    elif order == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    
    elif order == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
