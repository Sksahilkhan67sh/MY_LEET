from typing import List

class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)

        # pal[i][j] = True if s[i:j+1] is a palindrome
        pal = [[False] * n for _ in range(n)]

        # Length 1
        for i in range(n):
            pal[i][i] = True

        # Length 2 to n
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                if s[i] == s[j]:
                    if length == 2:
                        pal[i][j] = True
                    else:
                        pal[i][j] = pal[i + 1][j - 1]

        # dp[i] = max answer using first i characters
        dp = [0] * (n + 1)

        for end in range(1, n + 1):
            # Don't use a palindrome ending at end-1
            dp[end] = dp[end - 1]

            # Try every valid starting position
            for start in range(end - k, -1, -1):
                if pal[start][end - 1]:
                    dp[end] = max(
                        dp[end],
                        dp[start] + 1
                    )

        return dp[n]