from typing import List
from functools import lru_cache

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        # suffix[i] = sum of piles from i to the end
        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        @lru_cache(None)
        def dfs(i, m):
            # Can take all remaining piles
            if i + 2 * m >= n:
                return suffix[i]

            # Opponent's best possible score
            opponent = float("inf")

            for x in range(1, 2 * m + 1):
                opponent = min(
                    opponent,
                    dfs(i + x, max(m, x))
                )

            # Total remaining - opponent's score
            return suffix[i] - opponent

        return dfs(0, 1)