'''
Ch 8. Linked List
13. Palindrome Linked List (leetcode 234)
연결 리스트가 팰린드롬 구조인지 판별하라.
-> 앞뒤로 모두 추출할 수 있는 자료구조가 필요. 리스트의 pop()/pop(0)로 가능하다.

* Definition for singly-linked list -> Python에서는 필요없음.
class ListNode: 
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
'''

input1 = "1->2"  # 연결 리스트
input2 = "1->2->2->1"
node1 = list(map(int, input1.split('->'))) # 리스트로 변환
node2 = list(map(int, input2.split('->')))


# 1. 리스트 변환
import time
start = time.time()

def isPalindrome_list(node):
    if not node: 
        return True

    while len(node) > 1:
        if node.pop(0) != node.pop():
            return False
    return True

print('======= list ======')
print(f'Is it a Palindrome? : {isPalindrome_list(node1)}')
print(f'Is it a Palindrome? : {isPalindrome_list(node2)}')
print(f'Runtime: {time.time() - start} sec')


# 2. deque를 이용한 최적화
import collections
start = time.time()

def isPalindrome_deque(node):
    if not node:
        return True
    
    q = collections.deque(node)
    while len(q) > 1:
        if q.popleft() != q.pop():
            return False
    return True


print('======= deque ======')
print(f'Is it a Palindrome? : {isPalindrome_deque(node1)}')
print(f'Is it a Palindrome? : {isPalindrome_deque(node2)}')
print(f'Runtime: {time.time() - start} sec')


'''
- node.pop(0)
리스트는 맨 앞 아이템을 가져오기에 적합한 자료형이 아니다.
첫번째 값을 꺼내오면 모든 값이 한 칸씩 이동되므로 O(n) 발생

- deque.popleft()
deque는 이중 연결 리스트 구조로 양쪽 방향 모두 추출하는 데 O(1).
'''