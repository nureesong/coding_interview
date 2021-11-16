'''
Ch 6. String Manipulation
5. Group Anagrams (leetcode 49)
* 애너그램: 일종의 언어유희로 문자를 재배열하여 다른 뜻을 가진 단어로 바꾸는 것
문자열 배열을 받아 애너그램 단위로 그룹핑하라.
-> 각 단어를 알파벳 순으로 정렬하여 구성이 같은 단어끼리 묶는다.
'''
import collections

def groupAnagrams(input):
    groups = collections.defaultdict(list)
    
    for word in input:
        groups[''.join(sorted(word))].append(word)
    print(groups)
    
    return list(groups.values())

input = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(input))


'''
** 파이썬 기본 정렬: Timsort
a.sort(): a가 리스트인 경우만 가능!!
sorted(a): 리스트/문자열인 a를 정렬하여 리스트로 리턴 -> 다시 문자열로 결합하려면 join() 이용

** defaultdict(type): 존재하지 않는 키를 삽입할 때 발생하는 KeyError를 방지 **
'''