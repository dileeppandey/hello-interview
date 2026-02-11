"""
https://leetcode.com/problems/number-of-islands/

Given an m x n 2D binary grid which represents a map of '1's (land) and
'0's (water), return the number of islands. An island is surrounded by water
and is formed by connecting adjacent lands horizontally or vertically.

Example:
    grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    Output: 3
"""


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        # ------------------------------------------------------------------
        # DFS/BFS ON GRID INSIGHT: Each island is a connected component of
        # '1's. We scan the grid; when we find an unvisited '1', we've
        # discovered a new island. We then DFS/BFS to mark all connected
        # '1's as visited so we don't count them again.
        # ------------------------------------------------------------------

        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        count = 0

        def dfs(r: int, c: int) -> None:
            """Sink the entire island by marking connected '1's as '0'."""
            # Step A: Boundary check + water check
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
                return

            # Step B: Mark current cell as visited (sink it)
            grid[r][c] = '0'

            # Step C: Explore all 4 adjacent cells
            dfs(r + 1, c)  # down
            dfs(r - 1, c)  # up
            dfs(r, c + 1)  # right
            dfs(r, c - 1)  # left

        # Step 1: Scan every cell in the grid
        for r in range(rows):
            for c in range(cols):
                # Step 2: When we find a '1', it's a new island
                if grid[r][c] == '1':
                    count += 1
                    # Step 3: DFS to sink the entire island
                    dfs(r, c)

        return count


# ---- Quick verification ----
s = Solution()
grid1 = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]
print(s.numIslands(grid1))  # Expected: 1

grid2 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
print(s.numIslands(grid2))  # Expected: 3
