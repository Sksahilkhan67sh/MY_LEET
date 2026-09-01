from collections import defaultdict
from typing import List

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        last = defaultdict(list)
        ans = float("inf")

        for i, x in enumerate(nums):
            last[x].append(i)

            if len(last[x]) >= 3:
                # Three most recent occurrences
                distance = 2 * (last[x][-1] - last[x][-3])
                ans = min(ans, distance)

        return -1 if ans == float("inf") else ans