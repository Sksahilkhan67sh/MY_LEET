from typing import List
from collections import Counter

class Solution:
    def minSumSquareDiff(
        self,
        nums1: List[int],
        nums2: List[int],
        k1: int,
        k2: int
    ) -> int:
        k = k1 + k2
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]

        if sum(diff) <= k:
            return 0

        freq = Counter(diff)
        max_diff = max(diff)

        for d in range(max_diff, 0, -1):
            count = freq[d]
            if count == 0:
                continue

            next_count = freq[d - 1]
            cost = count

            if k >= cost:
                k -= cost
                freq[d - 1] += count
                freq[d] = 0
            else:
                # Reduce only k differences by one
                freq[d] -= k
                freq[d - 1] += k
                k = 0
                break

        return sum(d * d * count for d, count in freq.items())