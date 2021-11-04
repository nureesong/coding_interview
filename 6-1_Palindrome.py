"""
Ch 6. String Manipulation
1. Valid Palindrome (leetcode 125)
주어진 문자열이 팰린드롬인지 확인하라.
대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다.
"""

import re
import time
start = time.time()

def is_Palindrome(text):
    string = text.lower()
    string = re.sub('[^a-z0-9]', '', string)
    return string == string[::-1]  # 0.00012898
    # n = len(string)   # 0.00013494
    # for i in range(n//2):
    #     if string[i] != string[n-1-i]:
    #         return False
    # return True


print(is_Palindrome("A man, a plan, a canal: Panama"))
print(is_Palindrome("race a car"))
print(f'time: {time.time()-start}')

"""
문자열 슬라이싱: 내부적으로 C로 구현되어 있어 훨씬 빠른 속도.
문자열을 조작할 때는 항상 슬라이싱을 우선으로 사용하는 편이 속도 개선에 유리하다.
"""