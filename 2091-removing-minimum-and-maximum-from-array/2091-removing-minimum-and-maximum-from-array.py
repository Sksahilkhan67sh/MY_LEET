from typing import List

class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)

        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))

        # Put min_idx first and max_idx second
        if min_idx > max_idx:
            min_idx, max_idx = max_idx, min_idx

        # 1. Remove both from the left
        left = max_idx + 1

        # 2. Remove both from the right
        right = n - min_idx

        # 3. Remove min from left and max from right
        mixed = (min_idx + 1) + (n - max_idx)

        return min(left, right, mixed)