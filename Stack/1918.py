'''
BOJ 1918 후위 표기식
https://www.acmicpc.net/problem/1918
---

풀이법:
    INPUT: STRING
    SET: ANSWER: stack, STACK: stack, PRIORITY: hashtable
    연산자의 순위를 PRIORITY에 초기화함.
        */가 1순위, +-가 2순위, )가 3순위
    START for i = 0, 1, ..., len(string)
        if: string의 i-th element가 )라면,
            (가 나올 때가지 STACK에서 pop하여 ANSWER에 PUSH
        else if: string의 i-th element가 알파벳이라면,
            ANSWER에 PUSH
        else if: string의 i-th element가 (라면,
            STACK에 PUSH
        else if: string의 i-th element가 )라면,
            (전까지의 stack을 전부 다 pop하고
        else if: string의 i-th element가 연산자라면,
            stack내에 자기 이상의 우선순위를 갖는 연산자는 다 뱉음.
            (는 제외함.
            
문제점:
    input부터 FIFO구존데? 뒤로 쓸 수 있나? 
        -> for문으로 하면 FIFO가능
    어떻게 합치지? extend는 부담스럽고, 또 앞에다가 더하는건 어떻게 하지?
        -> print(end='')를 통해 한 줄로 이어서 출력이 가능.
'''

import sys

equation = sys.stdin.readline().rstrip()
equation = f"({equation})"
n = len(equation)

answer = []
stack = []
PRIORITY = {'*':2,
            '/':2,
            '+':1,
            '-':1,
            '(':0}

for i in range(n):
    num = equation[i]

    if num.isalpha():
        answer.append(num)
    
    elif num == '(':
        stack.append(num)
    
    elif num == ')':
        while stack:
            temp = stack.pop()
            
            if temp == "(":
                break
            answer.append(temp)
    else:
        while stack[-1] != '(' and PRIORITY[num] <= PRIORITY[stack[-1]]:
            temp = stack.pop()
            answer.append(temp)
        stack.append(num)

print("".join(answer))