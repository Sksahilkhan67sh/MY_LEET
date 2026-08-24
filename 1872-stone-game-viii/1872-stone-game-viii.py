from typing import List

class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)

        # Prefix sums
        for i in range(1, n):
            stones[i] += stones[i - 1]

        # If we take all remaining stones
        best = stones[-1]

        # Work backwards
        for i in range(n - 2, 0, -1):
            best = max(best, stones[i] - best)

        return best