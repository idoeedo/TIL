from typing import List


# ==============================================================================
# My Answer
# ==============================================================================
class MyAnswer:
    def numIslands(self, grid: List[List[str]]) -> int:
        pass


# ==============================================================================
# Solution 1
# ==============================================================================
class Solution1:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            if (
                i < 0
                or i >= len(grid)
                or j < 0
                or j >= len(grid[0])
                or grid[i][j] != "1"
            ):
                return

            grid[i][j] = "#"  # 방문했던 곳 마킹

            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1

        return count
