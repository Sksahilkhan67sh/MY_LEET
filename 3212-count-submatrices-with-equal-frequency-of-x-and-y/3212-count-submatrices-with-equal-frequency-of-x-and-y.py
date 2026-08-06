from typing import List

class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        x = [[0] * (n + 1) for _ in range(m + 1)]
        y = [[0] * (n + 1) for _ in range(m + 1)]

        ans = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                x[i][j] = (
                    x[i - 1][j]
                    + x[i][j - 1]
                    - x[i - 1][j - 1]
                    + (grid[i - 1][j - 1] == 'X')
                )

                y[i][j] = (
                    y[i - 1][j]
                    + y[i][j - 1]
                    - y[i - 1][j - 1]
                    + (grid[i - 1][j - 1] == 'Y')
                )

                if x[i][j] > 0 and x[i][j] == y[i][j]:
                    ans += 1

        return ans