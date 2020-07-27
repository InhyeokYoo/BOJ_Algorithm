'''
BOJ 11722 가장 긴 감소하는 부분 수열
https://www.acmicpc.net/problem/11722
---

- 풀이과정:
    - 뭔 소린가 싶었는데, 수열로 부분집합을 만들었을 때, decreasing 형태의 부분 수열 중 가장 긴 것의 길이를 묻는 문제이다.
    - **왜 DP로 풀어야 하는가?**  
        - dp[n]은 항상 감소하는 수열일 때, dp[n+i]에서 arr[n]을 추가하면 됨.
        - 즉, dp[n]의 길이는 dp[n+i] + 1
    - dp를 array의 부분집합으로 넣지말고, 그냥 길이로 생각해서 풀면 됨
    
'''
import sys

N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

dp = [1 for _ in range(N)]
answer = 1

for i in range(N-2, -1, -1):
    candidate = [0]
    for j in range(i+1, N):
        if arr[i] > arr[j]:
            candidate.append(dp[j])

    dp[i] = max(candidate) + 1

    if dp[i] >= answer:
        answer = dp[i]

print(answer)