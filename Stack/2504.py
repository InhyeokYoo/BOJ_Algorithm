'''
BOJ 2504 괄호의 값
https://www.acmicpc.net/problem/2504
---

9012번과 마찬가지로 전형적인 괄호쌍 문제. https://blog.encrypted.gg/936?category=773649
전반적으로 조잡하게 짠 감이 있는 것 같다.
'''

import sys

class Stack(list):
    def empty(self):
        if len(self) == 0:
            return True
        else:
            return False

    def top(self):
        if len(self) != 0:
            return self[-1]
        else:
            return -1

input = sys.stdin.readline().strip().split()
stack = Stack()
score = 0

for item in input:
    # Opend parenthesis
    if item == "(" or item == "[":
        stack.append(item)

    # Closed parenthesis
    else:
        if stack.empty():# is it VPS?
            print(0)
            return

        top = stack.top()
        if item == ")":
            # ( ) 의 경우 2점을 획득
            if top == "(":
                value = stack.pop()
                stack.append(2)
                continue

            # 숫자가 있다면 곱해야함.
            elif isinstance(top, int):
                nested = stack.pop()

                if stack.empty():
                    print(0)
                    return

                if stack.top() == "(":
                    stack.pop()
                    stack.append(nested * 2)

                elif isinstance(stack.top(), int):
                    while True:
                        top = stack.pop()

                        if stack.empty():
                            print(0)
                            return

                        nested += top
                        if not isinstance(stack.top(), int):
                            if stack.top() == "(":
                                stack.pop()
                                stack.append(nested*2)
                                break
                            else:
                                print(0)
                                return
                else:
                    print(0)
                    return
        elif item == "]":
            if top == "[":
                value = stack.pop()
                stack.append(3)
                continue
            elif isinstance(top, int):
                nested = stack.pop()
                if stack.empty():
                    print(0)
                    return
                if stack.top() == "[":
                    stack.pop()
                    stack.append(nested*3)
                elif isinstance(stack.top(), int):
                    while True:
                        top = stack.pop()
                        if stack.empty():
                            print(0)
                            return
                        nested += top
                        if not isinstance(stack.top(), int):
                            if stack.top() == "["
                                stack.pop()
                                stack.append(nested*3)
                                break
                            else:
                                print(0)
                                return
                else:
                    print(0)
                    return
else:
    for i in stack:
        if not isinstance(i, int):
            print(0)
            return
    print(sum(stack))