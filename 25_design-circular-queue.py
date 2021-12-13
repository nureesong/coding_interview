'''
Ch 9. Stack & Queue
25. Design Circular Queue (leetcode 622)
원형 큐를 디자인하라.
'''

class MyCircularQueue:
    def __init__(self, k):
        self.q = [None] * k
        self.maxlen = k
        self.front = 0
        self.rear = 0
        
    def enQueue(self, x):
        if self.q[self.rear]:
            return False
        # 여유 공간이 존재하면 요소 추가
        self.q[self.rear] = x
        self.rear = (self.rear + 1) % self.maxlen
        return True
        
    
    def deQueue(self):
        if self.q[self.front] == None:  # 원형큐가 비어있으면 deQueue할 수 없다
            return False
        # 비어있지 않으면 요소 제거
        self.q[self.front] = None
        self.front = (self.front + 1) % self.maxlen
        return True
    
    def Front(self):
        if self.q[self.front] == None:
            return -1
        else:
            return self.q[self.front]
    
    def Rear(self):
        if self.q[self.rear-1] == None:
            return -1
        else:
            return self.q[self.rear-1]
    
    def isFull(self):  
        # front와 rear가 같은 위치에서 만나고 그 위치에서 None이 아니면 가득 찬 것이다.
        return (self.front == self.rear) and (self.q[self.front] is not None)


circularQueue = MyCircularQueue(k=5)
print(circularQueue.enQueue(10))  # True
print(circularQueue.enQueue(20))  # True
print(circularQueue.enQueue(30))  # True
print(circularQueue.enQueue(40))  # True
print(circularQueue.Rear())       # 40
print(circularQueue.isFull())     # False
print(circularQueue.deQueue())    # True
print(circularQueue.deQueue())    # True
print(circularQueue.enQueue(50))  # True
print(circularQueue.enQueue(60))  # True
print(circularQueue.Rear())       # 60
print(circularQueue.Front())      # 30