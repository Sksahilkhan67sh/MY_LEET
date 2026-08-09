from typing import List

class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        ans = []

        for i in range(m - k + 1):
            row = []

            for j in range(n - k + 1):
                values = []

                # Collect the k x k submatrix values
                for r in range(i, i + k):
                    for c in range(j, j + k):
                        values.append(grid[r][c])

                # Sort values
                values.sort()

                # Find minimum difference between distinct values
                best = float("inf")

                for x in range(1, len(values)):
                    if values[x] != values[x - 1]:
                        best = min(best, values[x] - values[x - 1])

                # If all values are equal
                if best == float("inf"):
                    best = 0

                row.append(best)

            ans.append(row)

        return ans