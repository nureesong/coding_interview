'''
Ch 12. Graph
35. Combinations (leetcode 77)
전체 수 n을 입력받아 k개의 조합을 리턴하라.
'''
import time

def myCombine(n,k):
    results = []
    prev = []
    
    def dfs(elements):
        if (len(prev) == k) and (prev[::-1] not in results):
            results.append(prev[:])
        
        for e in elements:
            next = elements[:]
            next.remove(e)
            prev.append(e)
            
            dfs(next)
            prev.pop()
        
    dfs(list(range(1,n+1)))
    return results


def textbookCombine(n, k):
    results = []
    
    def dfs(elements, start, k):
        if k == 0:
            results.append(elements[:])
            # print(f">> Results = {results}\n")
        
        # 현재 값(start)보다 큰 정수 중 (k-1)개 선택하여 조합 생성
        for i in range(start, n+1):
            elements.append(i)
            # print(f"i={i}, elements={elements}")
            dfs(elements, i+1, k-1)
            elements.pop()
        
    dfs([], 1, k)
    return results


if __name__ == '__main__':
    n = 4
    k = 2

    print('\n======  My Solution  ======')
    start = time.time()
    print(myCombine(n,k))
    print(f"{time.time() - start} sec")
    
    print('\n======  Textbook Solution  ======')
    start = time.time()
    print(textbookCombine(n,k))
    print(f"{time.time() - start} sec")
