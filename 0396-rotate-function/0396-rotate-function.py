from typing import List

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)

        total = sum(nums)

        current = sum(i * nums[i] for i in range(n))

        ans = current

        for i in range(1, n):
            current = current + total - n * nums[n - i]
            ans = max(ans, current)

        return ans