'''
Ch 6. String Manipulation
6. Longest Palindrome Substring (leetcode 5)
가장 긴 팰린드롬 부분 문자열을 추출하라.
'''
import time

#----- My code -----
# 문자열 처음과 끝에서 점점 범위를 좁히며 탐색
start = time.time()

def longestPalindrome(string):
    subPalindrome = ''
    maxlen = 0
    
    for i in range(len(string)):
        substring = string[i:]
        
        while substring != substring[::-1]:
            substring = substring[:-1]
        
        if len(substring) > maxlen:
            subPalindrome = substring
            maxlen = len(substring)

    return subPalindrome

print("-----  My code  -----")
print(longestPalindrome("babad"))
print(longestPalindrome("cbbd"))
print(f'Runtime: {time.time()-start} sec')


#----- Two-pointer ------
# 팰린드롬 판별만 하면 되므로 매칭이 될 때 중앙을 중심으로 점점 확장하며 탐색
start = time.time()

def longestPalindrome_center(s):
    # 팰린드롬 판별 및 투포인터 확장
    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]

    # 해당 사항이 없을 때 빠르게 리턴
    if len(s) < 2 or s == s[::-1]:
        return s

    # 슬라이딩 윈도우 우측으로 이동
    result = ''
    for i in range(len(s)-1):
        result = max(result, expand(i,i+1), expand(i,i+2), key=len) # 짝,홀 모두 비교
    return result

print("-----  Two Pointer  -----")
print(longestPalindrome("babad"))
print(longestPalindrome("cbbd"))
print(f'Runtime: {time.time()-start} sec')
