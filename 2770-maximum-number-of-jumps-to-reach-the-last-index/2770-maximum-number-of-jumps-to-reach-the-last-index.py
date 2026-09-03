from typing import List

class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)

        # dp[i] = maximum jumps needed to reach index i
        dp = [-1] * n
        dp[0] = 0

        for j in range(1, n):
            for i in range(j):
                if dp[i] != -1 and abs(nums[i] - nums[j]) <= target:
                    dp[j] = max(dp[j], dp[i] + 1)

        return dp[n - 1]