'''
Ch 9. Stack & Queue
24. Implement Queue using Stacks (leetcode 232)

스택을 이용해 다음 연산을 지원하는 큐를 구현하라.
- push(x): 요소 x를 큐 마지막에 삽입한다.
- pop():큐 처음에 있는 요소를 제거한다.
- peek(): 큐 처음에 있는 요소를 조회한다.
- empty(): 큐가 비어 있는지 여부를 리턴한다.
'''

class MyQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []
        
    def push(self, x):
        if self.s2:
            while self.s2:
                self.s1.append(self.s2.pop())
        
        self.s1.append(x)
        # print('=== push ===')
        # print(f's1: {self.s1}')
    
    def pop(self):
        self.peek()
        return self.s2.pop()
            
    def peek(self):  
        # 재정렬 수행
        if not self.s2:
            for _ in range(len(self.s1)):
                self.s2.append(self.s1.pop())
        # print('=== peek ===' )
        # print(f's1: {self.s1}')
        # print(f's2: {self.s2}')
        return self.s2[-1]
    
    def empty(self):
        return (self.s1 == []) and (self.s2 == [])
    
    
queue = MyQueue()
queue.push(1)
queue.push(2)
print(queue.peek())  # 1
print(queue.pop())   # 1
print(queue.empty()) # False
queue.push(3)