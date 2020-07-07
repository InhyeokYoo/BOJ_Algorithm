'''
BOJ 10828 스택
https://www.acmicpc.net/problem/10828
'''

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