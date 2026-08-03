from typing import List
import heapq

class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])

        s1 = [[0] * (n + 1) for _ in range(m + 1)]
        s2 = [[0] * (n + 2) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                s1[i + 1][j + 1] = s1[i][j] + grid[i][j]
                s2[i + 1][j] = s2[i][j + 1] + grid[i][j]

        ans = set()

        for i in range(m):
            for j in range(n):
                ans.add(grid[i][j])

                k = 1
                while (
                    i - k >= 0 and
                    i + k < m and
                    j - k >= 0 and
                    j + k < n
                ):
                    total = 0

                    total += s1[i + 1][j + k + 1] - s1[i - k][j]
                    total += s2[i + 1][j - k] - s2[i - k][j + 1]
                    total += s2[i + k + 1][j] - s2[i][j + k + 1]
                    total += s1[i + k + 1][j + 1] - s1[i][j - k]

                    total -= (
                        grid[i - k][j] +
                        grid[i][j + k] +
                        grid[i + k][j] +
                        grid[i][j - k]
                    )

                    ans.add(total)
                    k += 1

        return heapq.nlargest(3, ans)