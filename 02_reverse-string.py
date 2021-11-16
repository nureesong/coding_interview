"""
Ch 6. String Manipulation
2. Reverse String (leetcode 344)
문자열을 뒤집는 함수를 작성하라. 입력값은 문자 배열이며, 리턴 없이 리스트 내부를 직접 조작하라.
"""


def reverseString(s):
    print(s[::-1])      # My code
    print(s.reverse())  # Pythonic method
    return


# Swapping with two-pointer
def reverseString(s):
    left, right = 0, len(s)-1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    print(s)


reverseString(["h", "e", "l", "l", "o"])
reverseString(["H","a","n","n","a","H"])

'''
reverse()는 리스트에만 제공된다. 
6-1처럼 문자열 슬라이싱 s = s[::-1] 을 사용하면 리트코드에서는 오류 발생
공간 복잡도를 O(1)로 제한하기 때문에 변수 할당을 처리하는 데 다소 제약이 있다.
-> s[:] = s[::-1]  ** 트릭 **
'''