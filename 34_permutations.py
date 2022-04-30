'''
Ch 12. Graph
34. Permutations (leetcode 46)
서로 다른 정수를 입력받아 가능한 모든 순열을 리턴하라.
'''

# [Method 1] DFS를 활용한 순열 생성
def permute(nums):
    print("=======  Using DFS  ========")
    results, prev = [], []
    
    def dfs(elements):
        # 재귀 종료 조건
        if len(elements) == 0:  # 모든 정수를 다 순회하면 생성된 순열 추가
            results.append(prev[:])  # prev의 사본 prev[:] 저장!!!!!
            print(f">> Results = {results}\n")
            return
            
        for e in elements:
            next = elements[:]
            next.remove(e)
            prev.append(e)
            print(f"e={e}, next={next}, prev={prev}")
            dfs(next)
            prev.pop()
        return
    
    dfs(nums)
    return results


# [Method 2] itertools를 활용한 순열 생성
import itertools
def permute_itertools(nums):
    print("\n=======  Using itertools  ========")
    return list(itertools.permutations(nums))


if __name__ == '__main__':
    input = [1,2,3]    
    
    print(permute(input))           # Method 1
    print(permute_itertools(input)) # Method 2
    
    
    
    


    
    