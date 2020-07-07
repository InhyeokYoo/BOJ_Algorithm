'''
BOJ 9012 괄호
https://www.acmicpc.net/problem/9012
---

전형적인 수식 괄호쌍 문제. https://blog.encrypted.gg/936?category=773649
'''

import sys

n = int(sys.stdin.readline())

for i in range(n):
    temp = sys.stdin.readline().rstrip()
    stack = []

    for item in temp: #(()())((()))
        if item == '(':
            stack.append(item)

        else: # )
            try:
                value = stack.pop()
                if value != "(":
                    print("NO")
                    break
            except IndexError:
                print("NO")
                break    
    else:
        if len(stack) == 0:
            print("YES")
        else:
            print("NO")