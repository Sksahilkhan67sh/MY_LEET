from typing import List

class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])

        # dp[j][c] = maximum score reaching column j
        # with exactly c cost
        dp = [[-1] * (k + 1) for _ in range(n)]

        # Starting cell is always 0
        dp[0][0] = 0

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                cost = 1 if grid[i][j] > 0 else 0
                value = grid[i][j]

                new_dp = [-1] * (k + 1)

                # From top
                if i > 0:
                    top = dp[j]

                    for c in range(cost, k + 1):
                        if top[c - cost] != -1:
                            new_dp[c] = max(
                                new_dp[c],
                                top[c - cost] + value
                            )

                # From left
                if j > 0:
                    left = dp[j - 1]

                    for c in range(cost, k + 1):
                        if left[c - cost] != -1:
                            new_dp[c] = max(
                                new_dp[c],
                                left[c - cost] + value
                            )

                dp[j] = new_dp

        ans = max(dp[n - 1])

        return ans