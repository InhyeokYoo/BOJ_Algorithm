'''
BOJ 2718 타일 채우기
https://www.acmicpc.net/problem/2718
---

- 풀이과정:
    - N의 크기가 주어지지 않았으므로, defaultdict을 사용함
    - 점화식을 못 세우겠음
    - dp[N]은,
        - dp[N-1]에 2x1 2개, 1x2 0개
        - -> dp[N-1] + dp[1]
        - dp[N-2]에 2x1 0개, 1x2 4개 -> + 1
        - dp[N-2]에 2x1 2개, 1x2 2개 -> + 4
        - dp[N-2]에 2x1 0개, 1x2 4개 -> + 1
        - -> dp[N-2] + dp[2] 인듯?
        - dp[N-3]에 2x1 4개, 1x2 2개
        - dp[N-3]에 2x1 2개, 1x2 2개
        - dp[N-3]에 2x1 4개, 1x2 2개
        - 이를 ->, <- 방향으로 삽입 가능
        - 중복되는 경우: 
    - 이건 너무 어렵다...
'''

import sys
from collections import defaultdict

T = int(sys.stdin.readline().rstrip())
dp = defaultdict(lambda : -1)
dp[0] = 0
dp[1] = 1
dp[2] = 5

def get_dp(n):
    if dp[n] < 0:
        if n % 2 == 0:
            return get_dp(n-2)
        else:
            return get_dp(n-2)
    else:
        return dp[n]

for i in range(T):
    N = int(sys.stdin.readline().rstrip())

