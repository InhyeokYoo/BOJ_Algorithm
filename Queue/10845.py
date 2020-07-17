'''
BOJ 10845 큐
https://www.acmicpc.net/problem/10845
---

- 풀이과정:
- 걍 하면 됨
'''

import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def empty(self):
        if self.size == 0:
            return 1
        else: 
            return 0

    def push(self, data):
        new_node = Node(data)
        
        if self.empty() == 1:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
        self.size += 1
    
    def pop(self):
        if self.empty() == 1:
            return -1
        else:
            temp = self.head
            self.head = temp.next
            if not self.head:
                self.tail = None
            temp.next = None
            self.size -= 1
            return temp.data
            
    def size(self):
        return self.size

    def front(self):
        if self.head:
            return self.head.data
        else:
            return -1

    def back(self):
        if self.tail:
            return self.tail.data
        else:
            return -1

q = Queue()
num = int(sys.stdin.readline().rstrip())

for i in range(num):
    order = sys.stdin.readline().rstrip().split()

    if order[0] == 'push':
        q.push(int(order[1]))
    elif order[0] == 'front':
        print(q.front())
    elif order[0] == 'back':
        print(q.back())
    elif order[0] == 'size':
        print(q.size)
    elif order[0] == 'empty':
        print(q.empty())
    elif order[0] == 'pop':
        print(q.pop())


