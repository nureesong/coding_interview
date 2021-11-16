'''
Ch 7. Array
9. 3Sum (leetcode 15)
배열을 입력받아 합으로 0을 만들 수 있는 3개의 엘리먼트를 출력하라.
'''
# nums = [-1,0,1,2,-1,-4]
nums = [-5,0,0,-1,0,1,3,2]


import time
start = time.time()

# 1. Brute-force: O(n^3)
def bruteForce(nums):
    answer = []
    N = len(nums)
    for i,a in enumerate(nums[:-2]):
        for j,b in enumerate(nums[i+1:-1]):
            c = -(a+b)
            if (c in nums) and (sorted([a,b,c]) not in answer):
                answer.append(sorted([a,b,c]))       
    return answer

print('======= Brute-force =======')
print(bruteForce(nums))
print(f'Runtime: {time.time()-start} sec')


# 2. Two-pointer: O(n^2)
start = time.time()
def twoPointer(nums):
    nums.sort()
    answer = []

    left, right = 0, len(nums)-1
    while left < right:
        sum = nums[left] + nums[right]
        if -sum in nums[left+1:right]:
            answer.append([nums[left], -sum, nums[right]])

        if sum < 0:    # right를 옮기면 sum이 더 작아지므로 더 큰 양수 필요.
            left += 1  # left를 옮겨야 |sum|이 0에 가까워짐
        else:
            right -= 1

    return answer

print('\n======= Two-pointer =======')
print(twoPointer(nums))
print(f'Runtime: {time.time()-start} sec')


# 3. Two-pointer (정답코드)
start = time.time()
def threeSum(nums):
    results = []
    nums.sort()

    for i in range(len(nums)-2):
        # 중복된 값 건너뛰기
        if i > 0 and nums[i] == nums[i-1]: continue

        # 간격을 좁혀가며 세 수의 합 계산
        left, right = i+1, len(nums)-1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            else: # sum = 0
                results.append([nums[i], nums[left], nums[right]])

                while left < right and nums[left] == nums[left+1]: # 중복된 값 건너뒤기
                    left += 1
                while left < right and nums[right] == nums[right-1]: # 중복된 값 건너뒤기
                    right -= 1
                
                left += 1
                right -= 1
    return results

print('\n======= Textbook =======')
print(threeSum(nums))
print(f'Runtime: {time.time()-start} sec')
            

