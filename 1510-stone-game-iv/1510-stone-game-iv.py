from functools import cache

class Solution:
    def winnerSquareGame(self, n: int) -> bool:

        @cache
        def dfs(x):
            if x == 0:
                return False

            i = 1

            while i * i <= x:
                # If we can move to a losing state,
                # current player wins.
                if not dfs(x - i * i):
                    return True

                i += 1

            return False

        return dfs(n)