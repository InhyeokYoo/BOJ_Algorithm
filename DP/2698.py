'''
BOJ 2698 인접한 비트의 갯수
https://www.acmicpc.net/problem/2698 
---

- 풀이과정:
    - **왜 DP로 풀어야 하는가?**
    -> $n$개의 배열에서 $k$개 만큼 인접한 경우의 수는 $n-1$의 배열에서 $k$개 만큼 인접한 경우의 수 $+ 0$ 이거나,
    $n-1$의 배열에서 $k-1$개 만큼 인접한 경우의 수 $+ 1$ 이므로 DP
    - 점화식은 어떻게 세울 수 있는가?
    -> n과 k, 그리고 마지막 숫자를 통해 점화식을 만들 수 있다.
    -> dp[n][k][0] = dp[n-1][k][1] + dp[n-1][k][0]
    -> dp[n][k][1] = dp[n-1][k-1][1] + dp[n-1][k][0]
'''

import sys

T = int(sys.stdin.readline().rstrip())

# Bottom-Up
dp = [[[0, 0] for _ in range(101)] for _ in range(101)]

# initialize
dp[1][0][0] = 1
dp[1][0][1] = 1

for n in range(2, 101):
    for k in range(n):
        dp[n][k][0] = dp[n-1][k][1] + dp[n-1][k][0]
        dp[n][k][1] = dp[n-1][k-1][1] + dp[n-1][k][0]

for i in range(T):
    n, k = list(map(int, sys.stdin.readline().rstrip().split()))
    print(sum(dp[n][k]))