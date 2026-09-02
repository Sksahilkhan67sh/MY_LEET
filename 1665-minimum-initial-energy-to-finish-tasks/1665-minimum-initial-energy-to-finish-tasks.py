from typing import List

class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        # Sort by (actual - minimum) ascending
        tasks.sort(key=lambda x: x[0] - x[1])

        ans = 0
        current = 0

        for actual, minimum in tasks:
            if current < minimum:
                needed = minimum - current
                ans += needed
                current += needed

            current -= actual

        return ans