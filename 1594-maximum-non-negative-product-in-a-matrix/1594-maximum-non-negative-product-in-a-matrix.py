from typing import List

class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7

        m = len(grid)
        n = len(grid[0])

        max_dp = [[0] * n for _ in range(m)]
        min_dp = [[0] * n for _ in range(m)]

        max_dp[0][0] = grid[0][0]
        min_dp[0][0] = grid[0][0]

        # First column
        for i in range(1, m):
            value = grid[i][0]
            max_dp[i][0] = max_dp[i - 1][0] * value
            min_dp[i][0] = min_dp[i - 1][0] * value

        # First row
        for j in range(1, n):
            value = grid[0][j]
            max_dp[0][j] = max_dp[0][j - 1] * value
            min_dp[0][j] = min_dp[0][j - 1] * value

        # Remaining cells
        for i in range(1, m):
            for j in range(1, n):
                value = grid[i][j]

                candidates = [
                    max_dp[i - 1][j] * value,
                    min_dp[i - 1][j] * value,
                    max_dp[i][j - 1] * value,
                    min_dp[i][j - 1] * value
                ]

                max_dp[i][j] = max(candidates)
                min_dp[i][j] = min(candidates)

        result = max_dp[m - 1][n - 1]

        if result < 0:
            return -1

        return result % MOD