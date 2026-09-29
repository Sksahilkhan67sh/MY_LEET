from typing import List
from functools import lru_cache


class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])

        # Path length must be even
        if (m + n - 1) % 2 == 1:
            return False

        # A valid parentheses string cannot start with ')'
        # or end with '('
        if grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False

        @lru_cache(None)
        def dfs(r, c, balance):
            if r >= m or c >= n:
                return False

            if grid[r][c] == '(':
                balance += 1
            else:
                balance -= 1

            # Invalid prefix
            if balance < 0:
                return False

            # Not enough cells left to close all open brackets
            remaining = (m - 1 - r) + (n - 1 - c)

            if balance > remaining:
                return False

            # Reached destination
            if r == m - 1 and c == n - 1:
                return balance == 0

            return (
                dfs(r + 1, c, balance)
                or dfs(r, c + 1, balance)
            )

        return dfs(0, 0, 0)