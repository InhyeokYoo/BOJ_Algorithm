'''
BOJ 6359 만취한 상범
https://www.acmicpc.net/problem/6359
---

- 풀이과정:
    - **왜 DP로 풀어야 하는가?**  
        - dp[n] = dp[n-1] + 1 if (n의 약수의 개수) % 2 == 1 (열림),  
        - otherwise dp[n] = dp[n-1] + 0 (닫힘)
    - 그럼 약수의 개수를 빠르게 파악하는 방법이 필요함.  
    걍 n//2 + 1까지만 한 후 + 1(n자기 자신)
'''

import sys

T = int(sys.stdin.readline().rstrip())
dp = [-1 for _ in range(101)]
dp[1] = 1

def top_down(n):
    if dp[n] < 0:
        cnt = 1
        for i in range(1, n//2+1):
            if n % i == 0:
                cnt += 1
        dp[n] = top_down(n-1) + 1 if cnt % 2 == 1 else top_down(n-1)
        return dp[n]
    else:
        return dp[n]

top_down(100)

for i in range(T):
    n = int(sys.stdin.readline().rstrip())

    print(dp[n])
    
