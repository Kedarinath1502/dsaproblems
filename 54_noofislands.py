'''
Given an m x n 2D binary grid grid which represents a map of '1's (land) 
and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands
horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        rows, cols = len(grid), len(grid[0])
        islands = 0

        def dfs(r,c):
            if (r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0"):
                return 
            grid[r][c] = "0"
            for nr, nc in directions:
                dfs(r+nr, c+nc)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    dfs(r,c)
                    islands += 1
        
        return islands
    

#bfs 
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        rows, cols = len(grid), len(grid[0])
        islands = 0
        def bfs(r,c):
            q = deque()
            grid[r][c] = "0"
            q.append((r,c))
            while q:
                pr, pc = q.popleft()
                for nr, nc in directions:
                    r = pr + nr
                    c = pc + nc
                    if (r<0 or c<0 or r>=rows or c>=cols or grid[r][c]=="0"):
                        continue
                    q.append((r,c))
                    grid[r][c] = "0"
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    bfs(r,c)
                    islands += 1
        return islands