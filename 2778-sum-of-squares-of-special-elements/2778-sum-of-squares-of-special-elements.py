from typing import List

class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        for i, num in enumerate(nums, start=1):
            if n % i == 0:
                ans += num * num

        return ans