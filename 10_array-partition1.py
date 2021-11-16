'''
Ch 7. Array
10. Array Partition (leetcode 561)
n개의 페어를 이용한 min(a,b)의 합으로 만들 수 있는 가장 큰 수를 출력하라.
(n쌍의 페어 = 배열 입력값은 항상 2n개)
'''

arr = [1,4,3,2]

# 1. Ascending order (Textbook)
# 정렬된 상태에서 오름차순으로 인접 요소 페어를 만들어 합한다.
pair = []
sums = 0
for n in sorted(arr):
    pair.append(n)
    if len(pair) == 2:
        sums += min(pair)
        pair = []
print(sums)


# 2. Theoretical method
# 오름차순 정렬 후 (1,2) (3,4) ... (n-1,n) 연속한 두 수를 묶으면 min의 총합이 최대가 된다.
# 즉, 짝수번째(인덱스 0부터니까) 숫자들의 합이 최댓값.
print(sum(sorted(arr)[::2]))
