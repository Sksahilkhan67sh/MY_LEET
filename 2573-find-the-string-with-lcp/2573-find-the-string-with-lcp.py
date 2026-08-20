from typing import List
from string import ascii_lowercase


class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)

        s = [""] * n

        # Construct the lexicographically smallest string.
        i = 0

        for c in ascii_lowercase:
            while i < n and s[i]:
                i += 1

            if i == n:
                break

            # If lcp[i][j] > 0, then s[i] == s[j].
            for j in range(i, n):
                if lcp[i][j] > 0:
                    s[j] = c

        # If some position is still unassigned,
        # more than 26 different characters are required.
        if "" in s:
            return ""

        # Verify the complete LCP matrix.
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):

                if s[i] == s[j]:

                    if i == n - 1 or j == n - 1:
                        # A suffix of length 1 has LCP exactly 1.
                        if lcp[i][j] != 1:
                            return ""

                    else:
                        # If first characters match:
                        # lcp[i][j] = 1 + lcp[i+1][j+1]
                        if lcp[i][j] != lcp[i + 1][j + 1] + 1:
                            return ""

                else:
                    # Different first characters means LCP must be 0.
                    if lcp[i][j] != 0:
                        return ""

        return "".join(s)