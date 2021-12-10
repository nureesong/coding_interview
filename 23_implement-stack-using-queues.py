'''
Ch 9. Stack & Queue
23. Implement Stack using Queues (leetcode 225)

큐를 이용해 다음 연산을 지원하는 스택을 구현하라.
- push(x): 요소 x를 스택에 삽입한다.
- pop(): 스택의 첫 번째 요소를 삭제한다.
- top(): 스택의 첫 번째 요소를 가져온다.
- empty(): 스택이 비어 있는지 여부를 리턴한다.
'''

import collections

class MyStack:
    def __init__(self):
        self.q = collections.deque()
        
    def push(self, x):
        self.q.append(x)
        # 큐는 첫 번째 원소만 조회/출력이 가능하다.
        # 따라서 스택에 push할 때부터 pop 수행을 고려하여
        # 가장 마지막에 입력한 원소를 출력할 수 있게 순서를 거꾸로 재정렬한다.
        for _ in range(len(self.q)-1):
            self.q.append( self.q.popleft() )
        
    def pop(self):
        return self.q.popleft()
    
    def top(self):
        return self.q[0]
    
    def empty(self):
        return len(self.q) == 0
    

stack = MyStack()
stack.push(1)
stack.push(2)
print(stack.top())    # 2
print(stack.pop())    # 2
print(stack.empty())  # False