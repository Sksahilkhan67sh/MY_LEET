class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:

        dp = [[0.0] * (r + 1) for r in range(query_row + 2)]

        dp[0][0] = float(poured)

        for i in range(query_row + 1):
            for j in range(i + 1):

                if dp[i][j] > 1:

                    overflow = (dp[i][j] - 1) / 2.0

                    dp[i + 1][j] += overflow
                    dp[i + 1][j + 1] += overflow

        return min(1.0, dp[query_row][query_glass])