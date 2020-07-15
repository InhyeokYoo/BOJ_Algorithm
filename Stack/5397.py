'''
5397 키로거
https://www.acmicpc.net/problem/5397
---

풀이법:

'''

import sys

num = int(sys.stdin.readline().rstrip())

for i in range(num):
    pwd = list()
    temp = list()

    input_ = sys.stdin.readline().rstrip()
    for item in input_:
        if item == "<":
            if len(pwd) != 0:
                temp.append(pwd.pop())
        elif item == ">":
            if len(temp) != 0:
                pwd.append(temp.pop())
        elif item == "-":
            if len(pwd) != 0:
                pwd.pop()
        else:
            pwd.append(item)
    temp.reverse()
    print("".join(pwd+temp))