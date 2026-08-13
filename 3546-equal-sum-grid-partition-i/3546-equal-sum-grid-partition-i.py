from typing import List

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        total = sum(sum(row) for row in grid)

        # Equal parts must have an even total sum.
        if total % 2 != 0:
            return False

        target = total // 2

        # Check horizontal cuts.
        prefix = 0

        for i in range(len(grid) - 1):
            prefix += sum(grid[i])

            if prefix == target:
                return True

        # Check vertical cuts.
        prefix = 0
        cols = len(grid[0])

        for j in range(cols - 1):
            for i in range(len(grid)):
                prefix += grid[i][j]

            if prefix == target:
                return True

        return False