from typing import List

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)

        # First house with a different color from the last
        i = 0
        while colors[i] == colors[-1]:
            i += 1

        # Last house with a different color from the first
        j = n - 1
        while colors[j] == colors[0]:
            j -= 1

        return max(n - 1 - i, j)