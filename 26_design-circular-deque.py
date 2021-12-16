'''
Ch 10. Deque & Priority Queue
26. Design Circular Deque (leetcode 641)
다음 연산을 제공하는 원형 데크를 디자인하라.

- MyCircularDeque(k): 데크 사이즈를 k로 지정하는 생성자
- insertFront()/insertLast(): 데크 처음/마지막에 아이템을 추가하고 성공할 경우 True 리턴
- deleteFront()/deleteLast(): 데크 처음/마지막에 아이템을 삭제하고 성공할 경우 True 리턴
- getFront()/getRear(): 데크의 첫 번째/마지막 아이템을 가져온다. 데크가 비어 있다면 -1 리턴
- isEmpty()/isFull(): 데크가 비어/가득 차 있는지 여부를 판별
'''

# class ListNode: 
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left, self.right = left, right


class MyCircularDeque:
    def __init__(self, k):
        self.head, self.tail = ListNode(None), ListNode(None)
        self.k = k    # max length
        self.len = 0  # current length
        self.head.right = self.tail
        self.tail.left = self.head
        
    # 이중 연결 리스트에 신규 노드 삽입
    def _add(self, node, new):
        n = node.right
        node.right = new
        new.left = node
        new.right = n
    
    def insertFront(self, x):
        if self.len == self.k:  # Full
            return False
        self._add(self.head, ListNode(x))
        self.len += 1
        return True
    
    def insertLast(self, x):
        if self.len == self.k:
            return False
        self._add(self.tail.left, ListNode(x))
        self.len += 1
        return True
    
    # 노드 제거
    def _del(self, node):
        n = node.right.right
        node.right = n
        n.left = node
        
    def deleteFront(self):
        if self.len == 0:
            return False
        self._del(self.head)
        self.len -= 1
        return True
    
    def deleteLast(self):
        if self.len == 0:
            return False
        self._del(self.tail.left.left)
        self.len -= 1
        return True
    
    def getFront(self):
        return self.head.right.val if self.len else -1
    
    def getRear(self):
        return self.tail.left.val if self.len else -1
    
    def isEmpty(self):
        return self.len == 0
    
    def isFull(self):
        return self.len == self.k
    

myCircularDeque = MyCircularDeque(3);
myCircularDeque.insertLast(1);  # True
myCircularDeque.insertLast(2);  # True
myCircularDeque.insertFront(3); # True
myCircularDeque.insertFront(4); # False, the queue is full.
myCircularDeque.getRear();      # 2
myCircularDeque.isFull();       # True
myCircularDeque.deleteLast();   # True
myCircularDeque.insertFront(4); # True
myCircularDeque.getFront();     # 4
