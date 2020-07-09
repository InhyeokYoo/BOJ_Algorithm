'''
BOJ 2493 탑
https://www.acmicpc.net/problem/2493
---

풀이법:
탑의 배열을 stack으로 준비한다. stack에서 하나씩 pop하며, stack에 남아있는 탑의 크기와 비교하면 된다.

1. 시간 초과 발생
- prev_hit, prev_hit_idx를 설정하여 이전에 적중한 탑의 크기와 idx를 기억했음.
- 도대체 어디서 시간을 잡아먹는 걸까?
- Pypy도 실패함.
import sys

num = int(sys.stdin.readline().strip()) # [1, 500,000]
stack = list(map(int, sys.stdin.readline().split())) # O(N)

answer = [0 for _ in range(num)] # O(N)
mn_fire = float('inf')
mx_fire = 0
prev_hit_idx = 0

while len(stack) != 1: # O(N)
    fire = stack.pop()

    record_idx = len(stack) # answer에 기록 용도
    hit_idx = len(stack) # hit 확인 용도
    
    if fire < mn_fire or record_idx <= prev_hit_idx:
        while hit_idx > 0: # O(N^2)
            hit_idx -= 1

            if stack[hit_idx] > fire:
                answer[record_idx] = hit_idx + 1 # hit_idx는 index이므로 +1을 해줌.
                mx_fire = stack[hit_idx]
                mn_fire = fire
                prev_hit_idx = hit_idx
                break
    else:
        answer[record_idx] = prev_hit_idx + 1
        
print(*answer)

import sys

num = int(sys.stdin.readline().strip()) # [1, 500,000]
array = list(map(int, sys.stdin.readline().split())) # O(N)
stack = []
answer = [0 for _ in range(num)] # O(N)

for idx, item in enumerate(array):
    if stack:
        while stack:
            if stack[-1][1] < item:
                stack.pop()
            else:
                # 수신탑 발견
                answer[idx] = stack[-1][0] + 1 # i번째 탑이므로 idx+1
                stack.append((idx, item))
                break
        else:
            answer[idx] = 0
            stack.append((idx, item))
    else:
        # 넣을 곳이 없음
        answer[idx] = 0
        stack.append((idx, item))
        
print(*answer)

'''


import sys

num = int(sys.stdin.readline().strip()) # [1, 500,000]
array = list(map(int, sys.stdin.readline().split())) # O(N)
stack = []
answer = [0 for _ in range(num)] # O(N)

for idx, item in enumerate(array):
    if stack:
        while stack:
            if stack[-1][1] < item:
                stack.pop()
            else:
                # 수신탑 발견
                answer[idx] = stack[-1][0] + 1 # i번째 탑이므로 idx+1
                stack.append((idx, item))
                break
        else:
            stack.append((idx, item))
    else:
        # 넣을 곳이 없음
        stack.append((idx, item))
        
print(*answer)


