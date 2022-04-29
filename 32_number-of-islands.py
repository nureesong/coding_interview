'''
Ch 12. Graph
32. Number of Islands (leetcode 200)
1을 육지로, 0을 물로 가정한 2D 그리드 맵이 주어졌을 때, 섬의 개수를 계산하라. 
(섬 = 연결되어 있는 1의 덩어리)
'''

# [Method 1] Using Recursion

def recursive_dfs(input, v, visited=[]):
    ''' v = (i,j) current position '''
    m, n = len(input), len(input[0])  # m: num_rows, n: num_cols
    visited.append(v)
    
    # Search Direction Order - Left, Right, Up, Down
    for dx, dy in zip([0,0,-1,1], [-1,1,0,0]):  
        nx, ny = v[0] + dx, v[1] + dy  # neighborhood of v
        
        # Index Validation
        if (nx < 0 or nx >= m) or (ny < 0 or ny >= n): continue
        
        if ((nx, ny) not in visited) and (input[nx][ny] == 1):  # Unvisited Island
            visited = recursive_dfs(input, (nx, ny), visited)
    
    return visited


if __name__ == '__main__':
    # Test Cases
    gridmap1 = [[1,1,1,1,0], [1,1,0,1,0], [1,1,0,0,0], [0,0,0,0,0]]
    gridmap2 = [[1,1,1,1,0], [1,1,0,1,0], [1,1,0,0,0], [0,0,0,0,1]]
    gridmap3 = [[1,1,1,1,0], [1,1,0,1,0], [1,1,0,0,0], [0,0,0,1,1]]
    gridmap4 = [[1,1,1,1,0], [1,1,0,1,0], [1,1,0,0,0], [0,0,1,0,1]]
    
    gridmaps = [gridmap1, gridmap2, gridmap3, gridmap4]
    answers = [1, 2, 2, 3]
    
    for k, (gridmap, answer) in enumerate(zip(gridmaps, answers)):
        print(f"\n-----  [Test Case {k+1}] -----") 
        
        visited = []
        cnt_islands = 0
        for i in range(len(gridmap)):
            for j in range(len(gridmap[0])):
                if (gridmap[i][j] == 1) and ((i,j) not in visited):   # Unvisited Island
                    visited = recursive_dfs(gridmap, (i,j), visited)
                    cnt_islands += 1
                
                    print(f"\nStart at ({i},{j})")
                    print(f"Visited position: {visited}")
                    print(f"Current Number of Islands: {cnt_islands}")
        
        print(f"\nDFS Result: {cnt_islands} -> {cnt_islands==answer}") 
        

# [Method 2] Using Stack Iteration