'''
Ch 8. Linked List
15. Reverse Linked List (leetcode 206)
연결 리스트를 뒤집어라.
'''

import collections
input = [1,2,3,4,5]

# 1. Recursion (leetcode)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not(head.next):
            return head.val
        
        # head.val, head.next = head.next, head.val
        print(f'before: {head}')
        head.val = self.reverseList(head.next)
        # head.val
        print(f'after: {head}')
        return head.val



# 2. For loop



