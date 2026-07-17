from typing import List
from collections import Counter
from itertools import accumulate
from bisect import bisect_right

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)

        freq = Counter(nums)

        cntG = [0] * (mx + 1)

        for g in range(mx, 0, -1):
            total = 0

            for multiple in range(g, mx + 1, g):
                total += freq[multiple]
                cntG[g] -= cntG[multiple]

            cntG[g] += total * (total - 1) // 2

        prefix = list(accumulate(cntG))

        return [bisect_right(prefix, q) for q in queries]