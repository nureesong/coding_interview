'''
Ch 6. String Manipulation
3. Reorder Log Files (leetcode 937)
로그를 재정렬하라. 기준은 다음과 같다.
1. 로그의 가장 앞 부분은 식별자다.
2. 문자로 구성된 로그가 숫자 로그보다 앞에 온다.
3. 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일할 경우 식별자 순으로 한다.
4. 숫자 로그는 입력 순서대로 한다.
'''


def reorderLogfiles(logs):
    # STEP 1: 문자/숫자로 구성된 로그 구분
    letters, digits = [], []
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)

    # STEP 2: 문자로 구성된 로그 정렬. 2개의 key 기준.
    letters.sort( key=lambda x: (x.split()[1:], x.split()[0]) )
    print(f"Sorted logs of letters: {letters}")

    return letters + digits


logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
print(f"Output: {reorderLogfiles(logs)}")

'''
a.sort: in-place 연산  vs  sorted(a): 원형 보존
a.sort(key=lambda x: (기준1, 기준2, ...))
'''