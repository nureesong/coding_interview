'''
Ch 7. Array
7. Two Sum (leetcode 1)
덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라.
'''

nums = [2, 7, 11, 15]
target = 9

# nums = [2, 7, 11, 15, 1, 9, 33, 24]
# target = 57


# 1. Brute-force: O(n^2)
import time
start = time.time()

def twosum_bf(nums, target):
    N = len(nums)
    for i in range(N-1):
        for j in range(i+1,N):
            if nums[i] + nums[j] == target:
                return [i,j]

print('----- Brute-force ------')
print(twosum_bf(nums=nums, target=target))
print(f'Runtime: {time.time() - start} sec')


# 2. 타켓과의 차를 이용한 탐색: O(n^2)이지만 brute-force보다 빠름
# target - nums[i]가 nums에 존재하는지 탐색
start = time.time()

def twosum_sub(nums, target):
    for i, a in enumerate(nums):  # O(n)
        b = target - a
        if b in nums[i+1:]:  # O(n)
            return [i, nums[i+1:].index(b) + (i+1)]

print('\n----- Subtract ------')
print(twosum_sub(nums=nums, target=target))
print(f'Runtime: {time.time() - start} sec')


# 3. 딕셔너리 활용: O(n) -> 시간 재보면 2,3번이 비슷함
start = time.time()

def twosum_dict(nums, target):
    # {key:값, value:인덱스}로 바꿔서 저장 -> O(n)
    nums_map = {}   # collections.defaultdict(int) 이게 더 느림!!
    for i, n in enumerate(nums):
        nums_map[n] = i
    
    # 타겟에서 i번째 수 a를 뺀 결과를 키로 조회 -> O(n)
    for a in nums:
        b = target - a
        if b in nums_map.keys():
            return [nums_map[a], nums_map[b]]

print('\n----- Dictionary + 2 for loops ------')
print(twosum_dict(nums=nums, target=target))
print(f'Runtime: {time.time() - start} sec')


# 4. 하나의 for문으로 조회 구조 개선
start = time.time()

def twosum_dict1(nums, target):
    nums_map = {}
    for i, a in enumerate(nums):
        nums_map[a] = i
        b = target - a
        if b in nums_map.keys():
            return [nums_map[b], nums_map[a]]

print('\n----- Dictionary + 1 for loop ------')
print(twosum_dict1(nums=nums, target=target))
print(f'Runtime: {time.time() - start} sec')