'''
Ch 8. Linked List
14. Merge Two Sorted Lists (leetcode 21)
정렬되어 있는 두 연결 리스트를 합쳐라. (정렬된 연결 리스트로 리턴!!)
'''

import collections
q1, q2 = [1,2,4], [1,3,4]
q3, q4 = [1,1,2,3], [2,4,6]
q5, q6 = [], [1,1,3]


# 1. while loop(My approach)
def mergeTwoLists(l1, l2):
    if not(l1) and not(l2):
        return None
    if not(l1):
        return collections.deque(l2)
    if not(l2):
        return collections.deque(l1)
    
    l1 = collections.deque(l1)
    l2 = collections.deque(l2)
    merged = collections.deque()
    
    i, j = l1.popleft(), l2.popleft()
    
    while l1 or l2:
        if i < j:
            merged.append(i)
            if not(l1): 
                merged.append(j)
                return merged + l2  
            i = l1.popleft()
        else:
            merged.append(j)
            if not(l2):
                merged.append(i)
                return merged + l1
            j = l2.popleft()
    
    merged.append(min(i,j))
    merged.append(max(i,j))
    return merged

print('======= while loop ========')
print(mergeTwoLists(q1,q2))
print(mergeTwoLists(q3,q4))
print(mergeTwoLists(q5,q6))


# 2. Recursion




'''
list끼리 또는 deque끼리는 + 로 병합 가능
list + deque는 TypeError 발생

'''