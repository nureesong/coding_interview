'''
Ch 8. Linked List
15. Reverse Linked List (leetcode 206)
연결 리스트를 뒤집어라.
'''

# 1-1. Recursion (vsc)
def reverse_recursion(list):
    if not(list):
        return []

    # print(f'before: {list}')
    rev = list[1:] + [list[0]]
    rev[:-1] = reverse_recursion(rev[:-1])
    # print(f'after: {rev}')
    return rev

print('\n====== Recursion ======')
input = [1,2,3,4,5]
print(f'output: {reverse_recursion(input)}')
input = [1,2]
print(f'output: {reverse_recursion(input)}')
input = []
print(f'output: {reverse_recursion(input)}')


# 2-1. While loop (vsc)
def reverse_while(list):
    rev = [0]*len(list)
    for i,n in enumerate(list):
        rev[-i-1] = n
    return rev

print('\n====== While Loop ======')
input = [1,2,3,4,5]
print(f'output: {reverse_while(input)}')
input = [1,2]
print(f'output: {reverse_while(input)}')
input = []
print(f'output: {reverse_while(input)}')


''' Executable Only in Leetcode
# 1. Recursion
def reverseList(self, head: ListNode) -> ListNode:
    def reverse(node: ListNode, prev: ListNode=None):
        if not node:
            return prev
        
        # next: 다음 재귀에서 첫번째 입력인 node에 해당.
        #       2-3-4-5-N / 3-4-5-N / 4-5-N / 5-N 순서로 맨앞 노드를 떼어낸다.
        # prev: 역순 연결리스트. None / 1-N / 2-1-N / ... / 5-4-3-2-1-N
        #       node.val을 그대로 두고 떼어낸 맨 앞 노드를 node.next로 덮어씌운다.
        next, node.next = node.next, prev 
        return reverse(next, node)
    
    return reverse(head)


# 2. While loop
def reverseList2(self, head: ListNode) -> ListNode:
    node, prev = head, None
    while node:
        next, node.next = node.next, prev 
        # next: 2-3-4-5-N / 3-4-5-N / 4-5-N / 5-N / None
        # node: 1-N / 2-1-N / 3-2-1-N / 4-3-2-1-N / 5-4-3-2-1-N
        
        prev, node = node, next
        # prev: 1-N / 2-1-N / 3-2-1-N / 4-3-2-1-N / 5-4-3-2-1-N
        # node: 2-3-4-5-N / 3-4-5-N / 4-5-N / 5-N / None
    
    return prev
'''

