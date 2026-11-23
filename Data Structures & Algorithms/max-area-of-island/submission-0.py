class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
        h = 0
        cur = 0
        
        def dfs(r, c):
            nonlocal cur
            if (r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != 1):
                return
            else:
                grid[r][c] = 0
                cur += 1
                for dr, dc in directions:
                    dfs(r + dr, c + dc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:                 
                    dfs(r, c)
                    h = max(h, cur)
                    cur = 0

        return h