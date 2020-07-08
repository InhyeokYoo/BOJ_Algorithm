'''
BOJ 1874 스택 수열
https://www.acmicpc.net/problem/1874
---

풀이법:
정답을 출력할 print_list와 수열을 저장할 stack을 준비한다. 정답 수열의 idx를 준비하여 하나씩 탐색할 준비를 한다.
1 부터 n까지 반복문에서 
    print_list에 +를 삽입하고 stack에 숫자를 삽입한다. 만일 이 숫자가 정답 배열을 맞출 경우, stack에서 pop한다.
    이후 stack에서 하나씩 pop하며 정답 배열과 비교한다.
반복문이 종료되면 남아있는 stack을 전부 다 pop 한다. 이때 정답 배열과 다를 경우 에러메시지를 출력하면 된다.
'''


import sys

# 입력
num = int(sys.stdin.readline().strip())
answer = [sys.stdin.readline().strip() for i in range(num)]
answer = list(map(int, answer))

stack = list() # [1, n] 수열을 임시적으로 저장할 저장소
print_list = list() # 결과물 print할 배열

idx = 0

for i in range(1, num+1):
    # 항상 먼저 push
    print_list.append("+")
    stack.append(i)
    
    # 정답과 같다면,
    if i == answer[idx]:
        stack.pop()
        print_list.append("-")
        idx += 1
        
        # 정답과 맞으면, stack 배열을 탐색해야 함.
        while stack: # 길이를 모르니까 stack만큼 
            if stack[-1] == answer[idx]:
                stack.pop()
                print_list.append("-")
                idx += 1
            else:
                break
        
else:
    # for문이 끝나면 임시 배열에서 모두 다 pop
    while stack:
        left_item = stack.pop()
        if left_item != answer[idx]:
            print("NO")
            break

        print_list.append("+")
    else:
        for item in print_list:
            print(item)