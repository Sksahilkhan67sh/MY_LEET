from typing import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        # Find sum of the longest sequential prefix
        total = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                total += nums[i]
            else:
                break

        # Find the smallest missing integer >= total
        seen = set(nums)

        while total in seen:
            total += 1

        return total