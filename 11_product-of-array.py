'''
Ch 7. Array
11. Product of Array Except Self (leetcode 238)
배열을 입력받아 output[i]가 자신을 제외한 나머지 모든 요소의 곱셈 결과가 되도록 출력하라.
단, 나눗셈을 하지 않고 O(n)에 풀이하라.
'''

nums = [1,2,3,4]

# 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
#           [1 2 3 4]
# 왼쪽 곱셈: 1 1 2 6 
# 오른쪽 곱셈:   24 12 4 1
# 요소별 곱셈: [1 1 2 6] * [24 12 4 1] = [24 12 8 6]

import time
start = time.time()

def myproduct(nums):
    left_prod, right_prod = [1]*len(nums), [1]*len(nums)
    
    for i in range(1,len(nums)):
        left_prod[i] = left_prod[i-1] * nums[i-1]
        right_prod[-i-1] = right_prod[-i] * nums[-i]

    return [x*y for x,y in zip(left_prod, right_prod)]

print(myproduct(nums))
print(f'Runtime: {time.time() - start} sec')  # 3.81e-5


# Textbook code
start = time.time()
def productExceptSelf(nums):
    out = []
    # 왼쪽 곱셈
    p = 1
    for i in range(len(nums)):
        out.append(p)
        p = p * nums[i]
    
    # 오른쪽 곱셈
    p = 1
    for i in range(len(nums)):
        out[-i-1] *= p
        p *= nums[-i-1]

    return out

print(productExceptSelf(nums))
print(f'Runtime: {time.time() - start} sec')  # 6.91e-6

'''
왼쪽, 오른쪽 곱셈 배열을 따로 구해서 곱하는 것보다
왼쪽 곱셈 배열을 구한 뒤, 오른쪽 방향은 바로 곱하는 게 4~5배 빠르다.
'''


# My approach: O(n^2)
# output = [1]*len(nums)
# for i,n in enumerate(nums):
#     for j in range(len(nums)):
#         if i == j:
#             continue
#         output[j] *= n
# print(output)