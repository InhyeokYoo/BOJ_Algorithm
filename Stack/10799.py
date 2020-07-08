import sys

stack = sys.stdin.readline().rstrip()
stick = [0]
cnt = 0
for i in range(len(stack)-1):
    if stack[i] == '(':
        if stack[i+1] == ")":
            # raisor
            cnt += stick[-1]
        else: # not raisor
            stick.append(stick[-1] + 1)
    else: 
        if stack[i-1] == "(": # raisor
            continue
        else: # End of floor
            cnt += 1
            stick.pop()
            
print(cnt+1) 