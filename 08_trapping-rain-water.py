'''
Ch 7. Array
8. Trapping Rain Water (leetcode 42)
높이를 입력받아 비 온 후 얼마나 많은 물이 쌓일 수 있는지 계산하라.
'''

# 1. Two Pointer: 높이가 최대인 지점에서 좌우 포인터가 서로 만난다. O(n)
def twopointer(height):
    if not height:
        return 0

    volume = 0
    left, right = 0, len(height)-1
    left_max, right_max = height[left], height[right]
    
    while left < right:
        left_max = max(left_max, height[left])
        right_max = max(right_max, height[right])
        
        if left_max <= right_max:
            volume += left_max - height[left]
            left += 1
        else:
            volume += right_max - height[right]
            right -= 1 
    
    return volume

height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(f'Two-pointer Method: {twopointer(height)}')

'''
l,r  l,r_max    volume
0,11   0,1   0 + (0-0) = 0
1,11   1,1   0 + (1-1) = 0
2,11   1,1   0 + (1-0) = 1
3,11   2,1   1 + (1-1) = 1
3,10   2,2   1 + (2-2) = 1
4,10   2,2   1 + (2-1) = 2
5,10   2,2   2 + (2-0) = 4
6,10   2,2   4 + (2-1) = 5
7,10   3,2   5 + (2-2) = 5
7,9    3,2   5 + (2-1) = 6
7,8    3,2   6 + (2-2) = 6
'''


# 2. Stack: O(n)
# 스택에 쌓아 나가면서 현재 높이가 이전 높이보다 높을 때, 변곡점 기준으로 격차만큼 물 높이를 채운다.

def stacking(height):
    if not height:
        return 0
    
    volume = 0
    stack = []

    for i in range(len(height)):
        # print(f'\n====== i = {i} ======')
        
        # 변곡점을 만나는 경우 = 현재가 이전보다 높을 때
        while stack and height[i] > height[stack[-1]]:
            # print(f'stack: {stack}')
            top = stack.pop()

            if not len(stack):
                # print('stack is empty!')
                break
            
            # 이전과의 차이만큼 물 높이 처리
            distance = i - stack[-1] -1
            waters = min(height[i], height[stack[-1]]) - height[top]
            volume += distance * waters
            # print(f'Current volume: {distance}*{waters} | Total volume: {volume}')
        
        stack.append(i)
        # print(f'stack: {stack}')
    return volume
    

height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(f'Stacking Method: {stacking(height)}')

''''
====== i = 0 ======
stack: [0]

====== i = 1 ======
stack: [0]
stack is empty!
stack: [1]

====== i = 2 ======
stack: [1, 2]

====== i = 3 ======
stack: [1, 2]
Current volume: 1*1 | Total volume: 1
stack: [1]
stack is empty!
stack: [3]

====== i = 4 ======
stack: [3, 4]

====== i = 5 ======
stack: [3, 4, 5]

====== i = 6 ======
stack: [3, 4, 5]
Current volume: 1*1 | Total volume: 2
stack: [3, 4, 6]

====== i = 7 ======
stack: [3, 4, 6]
Current volume: 2*0 | Total volume: 2
stack: [3, 4]
Current volume: 3*1 | Total volume: 5
stack: [3]
stack is empty!
stack: [7]

====== i = 8 ======
stack: [7, 8]

====== i = 9 ======
stack: [7, 8, 9]

====== i = 10 ======
stack: [7, 8, 9]
Current volume: 1*1 | Total volume: 6
stack: [7, 8, 10]

====== i = 11 ======
stack: [7, 8, 10, 11]
'''