'''
Ch 6. String Manipulation
4. Most Common Word (leetcode 819)
금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라.
대소문자 구분을 하지 않으며, 구두점(마침표, 쉼표 등) 또한 무시한다.
'''

import re
import collections

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

def mostCommonWord(paragraph, banned):
    counts = collections.defaultdict(int)
    for word in paragraph.lower().split():
        word = re.sub('[^a-z]', '', word)
        
        if word in banned:
            continue
        
        counts[word] += 1
    print(counts)

    return max(counts, key=counts.get)  # argmax

print("----- My code -----")
print(f'The most common word: {mostCommonWord(paragraph, banned)}')


# List Comprehension, Counter
def mostCommonWord_another(paragraph, banned):
    # Data cleansing
    words = [ word for word in re.sub('[\W]', ' ', paragraph).lower().split() if word not in banned ]  
    # print(words)

    counts = collections.Counter(words)
    print(counts)
    return counts.most_common(1)[0][0] # counts.most_common(1) : [(str, num)]

print("----- Another method ----")
print(f'The most common word: {mostCommonWord_another(paragraph, banned)}')

'''
[자료구조 - 딕셔너리]
dict(): key 존재유무 확인 후 초기화 필수
defaultdict(int): key 존재유무 확인 불필요
value 기준 정렬: sorted(counts.items(), key=operator.itemgetter(1), reverse=True)
** 딕셔너리로 등장 횟수를 카운트하면 정렬이 안 되어 있다.
-> collections.Counter() 이용 시 value 기준 내림차순 정렬까지 한꺼번에 가능함!!

[정규표현식] 
\w : 단어 문자(word) 의미. 알파벳/숫자/_ 중 한 문자.
\W = ^\w: non-word 의미. 알파벳/숫자/_ 가 아닌 문자.
'''