from typing import List

class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n = len(word1)
        m = len(word2)

        # last[j] = latest index in word1 from which
        # word2[j:] can still be matched exactly.
        last = [-1] * m

        i = n - 1
        j = m - 1

        while i >= 0 and j >= 0:
            if word1[i] == word2[j]:
                last[j] = i
                j -= 1
            i -= 1

        ans = []
        j = 0
        canSkip = True

        for i in range(n):
            if j == m:
                break

            # Exact match
            if word1[i] == word2[j]:
                ans.append(i)
                j += 1

            # Use the one allowed mismatch
            elif canSkip:
                # We can use i as the mismatch only if
                # word2[j+1:] can still be matched after i.
                if j == m - 1 or i < last[j + 1]:
                    ans.append(i)
                    j += 1
                    canSkip = False

        return ans if j == m else []