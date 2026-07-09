class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def dfs(r, c):
            if (r, c) in visited: return 0
            if r > ROWS - 1 or r < 0 or c > COLS - 1 or c < 0 or grid[r][c] == 0: 
                return 1
            visited.add((r, c))
            
            res = dfs(r + 0, c + 1) + dfs(r + 0, c + -1) + dfs(r + 1, c + 0) + dfs(r + -1, c + 0)
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return dfs(r, c)