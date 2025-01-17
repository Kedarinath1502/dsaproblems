'''
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) 
connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid 
are surrounded by water.
The area of an island is the number of cells with a value 1 in the island.
Return the maximum area of an island in grid. If there is no island, return 0.
'''
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols  = len(grid), len(grid[0])
        maxi = 0
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        
        def dfs(r,c):
            nonlocal res
            if (r<0 or c<0 or r>=rows or c>=cols or grid[r][c] == 0):
                return
            res += 1
            grid[r][c] = 0
            for nr, nc in directions:
                dfs(r+nr, c+nc)
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    res = 0
                    dfs(r,c)
                    maxi = max(maxi, res)
        return maxi