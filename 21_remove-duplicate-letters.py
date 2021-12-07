'''
Ch 9. Stack & Queue
21. Remove Duplicate Letters (leetcode 316)
중복된 문자를 제외하고 사전식 순서로 나열하라.
'''

import collections

input1 = "bcabc"
input2 = "cbacdcbc"

def removeDuplicateLetters(s):
    print(f'\n========  [START] Input: {s}  ==========')
    counter = collections.Counter(s)
    stack, seen = [], set()  
    # stack은 검색/조화가 불가능 -> 이미 처리된 문자를 확인하기 위해 seen 변수를 활용한다.
    # 즉, seen에는 현재 stack에 포함되어 있는 문자가 담겨있다.
    
    for char in s:
        print(f'\n--- Current character is {char} ---')
        counter[char] -= 1
        # print(counter)
        print(f'Before while loop - stack = {stack}, seen = {seen}')
        
        # 이미 처리된 문자는 스킵한다. 
        if char in seen:
            print('Already seen character. Skip!')
            continue
        
        # 현재 문자가 이전 문자보다 알파벳 순서상 앞이고,
        # 이전 문자의 카운트가 남아서 나중에 또 등장한다면 스택에서 제거
        while stack and (char < stack[-1]) and counter[stack[-1]] > 0:
            seen.remove(stack.pop())
            print(f'   In while loop - stack = {stack}, seen = {seen}')
        
        # stack에는 중복문자가 제거되어 사전식 순서로 쌓이게 된다.
        stack.append(char)
        seen.add(char)
        print(f'After while loop - stack = {stack}, seen = {seen}')
        
    return ''.join(stack)

print(f'\n========  [END] Input: {input1} -> Output: {removeDuplicateLetters(input1)}  ==========\n')
print(f'\n========  [END] Input: {input2} -> Output: {removeDuplicateLetters(input2)}  ==========\n')


'''
- 문자끼리 순서 비교 가능
"a" < "b"  ->  True 

- 문자별 개수 자동 카운팅 (딕셔너리로 for문 돌리지 말 것!)
counter = collections.Counter(string)
'''