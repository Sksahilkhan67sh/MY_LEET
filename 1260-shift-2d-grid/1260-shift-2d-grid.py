from typing import List

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:

        m = len(grid)
        n = len(grid[0])

        arr = []

        for row in grid:
            arr.extend(row)

        total = m * n
        k %= total

        arr = arr[-k:] + arr[:-k]

        ans = []

        idx = 0

        for _ in range(m):
            ans.append(arr[idx:idx + n])
            idx += n

        return ans