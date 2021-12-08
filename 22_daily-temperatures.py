'''
Ch 9. Stack & Queue
22. Daily Temperatures (leetcode 739)
매일의 화시 온도 리스트 T를 입력받아서, 더 따듯한 날씨를 위해서는 며칠을 더 기다려야 하는지를 출력하라.

* Stack 사용: O(n)  (08_trapping-rain-water 문제 참고)
현재 온도가 이전보다 낮으면 계속해서 스택한다.
현재 온도가 더 높으면, 더 낮은 온도를 계속해서 pop한다. 하노이 탑처럼 더 높은 걸 위에 쌓을 수 없다.
'''

T = [73, 74, 75, 71, 69, 72, 76, 73]

def dailyTemperatures(T):    
    wait = [0]*len(T)  # T=[] -> wait = [0]*0 = [] 예외처리 필요없음
    stack = []
    
    for i, today in enumerate(T):
        print(f"\n Day {i} temperature is {today}")
        
        # 현재가 이전보다 높을 때
        while stack and today > T[stack[-1]]:
            top = stack.pop()
            wait[top] = i - top 
        stack.append(i)
        
        print(f'stack: {stack}')
        print(f' wait: {wait}')
    return wait
    
print('\n=========  Stacking Method  =========')
print(f'\n >> Output : {dailyTemperatures(T)}')
print('='*40)


''' 
* Brute-force: 오늘보다 더 높은 온도가 나왔을 때의 인덱스와 현재 인덱스 차이를 구한다. O(n^2)
def bruteForce(T):
    wait = []
    for i, today in enumerate(T):
        day = 0
        print(f"\nToday's temperature: {today}")
        for j in range(i+1, len(T)):
            if today < T[j]:
                day = j - i
                break
        wait.append(day)
    return wait

print(bruteForce(T))
'''