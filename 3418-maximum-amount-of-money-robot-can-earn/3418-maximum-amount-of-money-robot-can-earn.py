from typing import List

class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m = len(coins)
        n = len(coins[0])

        NEG = -10**18

        # dp[j][k]:
        # maximum amount reaching current row's column j
        # with k neutralizations remaining
        dp = [[NEG] * 3 for _ in range(n)]

        for i in range(m):
            for j in range(n):
                value = coins[i][j]

                if i == 0 and j == 0:
                    dp[j][0] = value
                    dp[j][1] = 0 if value < 0 else value
                    dp[j][2] = 0 if value < 0 else value
                    continue

                old = dp[j][:]

                # Values from top
                top = old

                # Values from left
                left = dp[j - 1] if j > 0 else [NEG] * 3

                for k in range(3):
                    best = max(top[k], left[k])

                    # Don't neutralize current cell
                    if best != NEG:
                        dp[j][k] = best + value
                    else:
                        dp[j][k] = NEG

                # Neutralize current negative cell
                if value < 0:
                    for k in range(1, 3):
                        best = max(top[k - 1], left[k - 1])

                        if best != NEG:
                            dp[j][k] = max(
                                dp[j][k],
                                best
                            )

        return dp[n - 1][2]