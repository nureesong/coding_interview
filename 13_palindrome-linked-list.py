'''
Ch 8. Linked List
13. Palindrome Linked List (leetcode 234)
연결 리스트가 팰린드롬 구조인지 판별하라.
-> 앞뒤로 모두 추출할 수 있는 자료구조가 필요. 리스트의 pop()/pop(0)로 가능하다.
'''

# Definition for singly-linked list -> Python에서는 필요없음.
# class ListNode: 
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


def isPalindrome(node):
    if not node: 
        return True

    # 리스트로 변환 -> Python에서는 필요없음.
    # node = head
    # q = []
    # while node is not None:
    #     q.append(node.val)
    #     node = node.next

    # 팰린드롬 판별
    while len(node) > 1:
        if node.pop(0) != node.pop():
            return False
    return True


# input = "1->2"  # 연결 리스트
input = "1->2->2->1"

# 리스트로 변환
node = list(map(int, input.split('->')))
print(node)

print(f'Is it a Palindrome? : {isPalindrome(node)}')