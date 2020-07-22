'''
BOJ 9507 Generations of Tribbles
https://www.acmicpc.net/problem/9507
---

- 풀이과정:
    - **왜 DP로 풀어야 하는가?**
    걍 딱 봐도 피보나치...  

'''

from collections import defaultdict
import sys

t = int(sys.stdin.readline().rstrip())

dp = defaultdict(int)
dp[0] = 1
dp[1] = 1
dp[2] = 2
dp[3] = 4

def get_dp(n):
    if dp[n-1] == 0:
        get_dp(n-1)
    if dp[n-2] == 0:
        get_dp(n-2)
    if dp[n-3] == 0:
        get_dp(n-3)
    if dp[n-4] == 0:
        get_dp(n-4)
    dp[n] = dp[n-1] + dp[n-2] + dp[n-3] + dp[n-4]

for i in range(t):
    n = int(sys.stdin.readline().rstrip())
    if dp[n] == 0:
        get_dp(n)
        print(dp[n])
    else:
        print(dp[n])