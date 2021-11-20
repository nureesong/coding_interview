'''
Ch 9. Stack & Queue
20. Valid Parentheses (leetcode 20)
괄호로 된 입력값이 올바른지 판별하라.
'''


def validParentheses(input):
    stack = []
    dict = {'(': ')', '[': ']', '{': '}'}

    for p in input:
        if p in dict.keys():
            stack.append(p)
        elif (not stack) or (dict[stack.pop()] != p):
            return False
    
    return len(stack) == 0  # 예외처리


print('\n===== Test cases =====')
s = '()[]{}'
print(f'Input: {s} -> Output: {validParentheses(s)}')
s = '()'
print(f'Input: {s} -> Output: {validParentheses(s)}')
s = '(]'
print(f'Input: {s} -> Output: {validParentheses(s)}')
s = '([)]'
print(f'Input: {s} -> Output: {validParentheses(s)}')
s = '{[]}'
print(f'Input: {s} -> Output: {validParentheses(s)}')
s = ''  # 예외처리!!
print(f'Input: {s} -> Output: {validParentheses(s)}')
