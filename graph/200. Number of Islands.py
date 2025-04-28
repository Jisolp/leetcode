from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        rows , cols = len(grid), len(grid[0])
        island = 0 
        def dfs(r,c):
            if (r < 0 or r >= rows or c < 0 or c >= cols or (r,c) in visited or grid[r][c] != "1"):
                return False
            visited.add((r,c))
            dfs(r+1,c) 
            dfs(r-1,c) 
            dfs(r,c+1) 
            dfs(r,c-1)
        for r in range(rows):
            for c in range(cols):
                if (r,c not in visited and grid[r][c] == "1"):
                    dfs((r,c))
                    island += 1
        return island
        # visited = set()
        # rows, cols = len(grid), len(grid[0])
        # island = 0 

        # def bfs(r,c):
        #     q = deque()
        #     q.append((r,c))
        #     visited.add((r,c))
        #     while q:
        #         row,col = q.popleft()
        #         directions = [(1,0),(0,1),(-1,0),(0,-1)]
        #         for dr, dc in directions:
        #             r = row+dr
        #             c = col+dc
        #             if (r in range(rows) and c in range(cols) and 
        #               grid[r][c] == "1" and (r,c) not in visited): 
        #                 q.append((r,c))
        #                 visited.add((r,c))
        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == "1" and (r,c) not in visited:
        #             bfs(r,c)
        #             island += 1
        # return island