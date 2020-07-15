'''
9935 문자열 폭발
https://www.acmicpc.net/problem/9935
---

풀이법:
- 그냥 풀게 될 경우 시간복잡도가 매우 크게 증가한다. 따라서 stack을 이용해야 한다.
- INPUT: string, bomb
- SET: TEMP
- for i = 1, ..., length of string
    - string의 i-th 원소를 temp에 push한다.
    - string의 i-th 원소를 폭탄의 마지막 문자와 비교한다.
    - 맞다면,
        - temp의 뒤에서부터 폭탄 문자열의 길이만큼과 폭탄을 비교한다.
            - 맞다면 temp를 pop하여 폭탄을 제거함.
- end loop

문제점:
- O(N)으로도 시간초과가 발생
    O(N)을 더 줄여보자
'''

import sys

string = sys.stdin.readline().rstrip()
bomb = list(sys.stdin.readline().rstrip()) # O(36)

n = len(bomb)

temp = list(string[:n-1])

for i in range(n-1, len(string)): # O(1,000,000)
    temp.append(string[i])

    if string[i] == bomb[-1]:
        # TODO: 검사
        if temp[-n:] == bomb:
            for i in range(n):
                temp.pop()
else:
    if temp:
        print("".join(temp))
    else:
        print('FRULA')

# import sys

# string = list(sys.stdin.readline().rstrip()) # O(1,000,000)
# bomb = list(sys.stdin.readline().rstrip()) # O(36)
# bomb.reverse() # O(36)

# n = len(bomb)
# temp = []

# while string: # O(1,000,000)
#     temp.append(string.pop())
    
#     if temp[-n:] == bomb: # O(36)
#         temp = temp[:-n] # O(36)
# else:
#     if temp:
#         temp.reverse() # O(1,000,000)
#         print(*temp)
#     else:
#         print('FRULA')


# import sys
# import re

# string = sys.stdin.readline().rstrip()
# bomb = sys.stdin.readline().rstrip()
# n = len(bomb)

# p = re.compile(bomb)

# loop_ctr = True

# while loop_ctr:
#     if p.search(string):
#         string = p.sub('', string)
#     else:
#         loop_ctr = False

# if string:
#     print(string)
# else:
#     print('FRULA')