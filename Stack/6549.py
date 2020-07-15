'''
6549 히스토그램에서 가장 큰 직사각형
https://www.acmicpc.net/problem/6549
---

풀이법: 길이를 넣다가 더 작은게 들어오면 pop해서 그때 계산하는 방법. 이러려면 idx를 통해 가로길이를 세야 함.
- 0: stack: [(0, 2)]. 처음엔 그냥 넣음.
- 1: stack: [(0, 2)]. (1, 1). 
    - 2 > 1 이므로 
        - 2를 pop. 넓이: 2 x (1 - 0) = 2. 
    - (1, 1)은 pop된 데이터의 idx로 바꿔줌. (0, 1)append.
- 2: stack: [(0, 1)]. 1 < 4 이므로 그냥 append.
- 3: stack: [(0, 1), (2, 4)]. 4 < 5 이므로 그냥 append.
- 4: stack: [(0, 1), (2, 4), (3, 5)]. 
    - 5 > 1 이므로 
        - 5를 pop. 넓이: 5 * (4 - 3)
    - 4 > 1 이므로 
        - 4를 pop. 넓이: 4 * (4 - 2)
    - (4, 1)은 pop된 데이터의 idx로 바꿔줌. (2, 1) append.
...

- 문제점:
    - 내림차순으로 들어오면 큰 것들은 이미 pop했기 때문에 계산이 안됨.
    따라서 마지막으로 pop한 (히스토그램에선 맨 앞) 자리에 값을 넣어줘야 함.

    - 마지막은 iteration이 안돌아감. 따라서 배열에 [0]을 넣어줌.

    - max(area)에서 런타임 에러 발생. 아무래도 empty인 경우를 생각해야 할 듯.
'''

import sys

while True:
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    if arr[0] == 0:
        break
    n, arr = arr[0], arr[1:] + [0]

    stack = list()
    mx = 0

    for i, item in enumerate(arr):
        if len(stack) == 0:
            stack.append((i, item))
            continue

        if stack[-1][1] <= item:
            stack.append((i, item))
        else:
            while stack and stack[-1][1] > item:
                temp = stack.pop()
                mx = max(mx, (temp[1] * (i - temp[0])))
                
            stack.append((temp[0], item))

    print(mx)