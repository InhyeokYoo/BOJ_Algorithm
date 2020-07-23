'''
BOJ 2163 초콜릿 자르기
https://www.acmicpc.net/problem/2163
---

- 풀이과정:
    - 목표: 초콜릿을 쪼개는 횟수를 최소화 -> 점화식이 되야 함.
    - 점화식: dp[n][m] = min(dp[1][m] + dp[n-1][m], dp[2][m] + dp[n-2][m], ..., dp[n-1][m] + dp[n1][m], # row로 쪼갬
                            dp[n][1] + dp[n][m-1], dp[n][m-2] + dp[n][m-2], ..., dp[n][m] + dp[n1][m-1],) # col로 쪼갬
    - 여기서 중복되는게 있으므로, diagonal을 포함한 lower/upper matrix만 계산하면 된다.
'''

import sys

N, M = list(map(int, sys.stdin.readline().rstrip().split()))

dp = [[-1 for _ in range(M+1)] for _ in range(N+1)]

def call_dp(n, m):
    if dp[n][m] > 0:
        return dp[n][m]
    elif n == 1 and m == 1:
        return 0
    elif n == 1:
        dp[n][m] = call_dp(n, 1) + call_dp(n, m-1) + 1
        return dp[n][m]
    else:
        dp[n][m] = call_dp(1, m) + call_dp(n-1, m) + 1
        return dp[n][m]
    
call_dp(N, M)
print(dp[N][M])