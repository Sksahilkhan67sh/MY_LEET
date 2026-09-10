from typing import List

class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)

        ans = [0] * n

        # pre_max[i] = maximum value in nums[0..i]
        pre_max = [0] * n
        pre_max[0] = nums[0]

        for i in range(1, n):
            pre_max[i] = max(pre_max[i - 1], nums[i])

        # Minimum value strictly to the right of i
        suf_min = float('inf')

        for i in range(n - 1, -1, -1):

            if i == n - 1:
                ans[i] = pre_max[i]
            elif pre_max[i] > suf_min:
                ans[i] = ans[i + 1]
            else:
                ans[i] = pre_max[i]

            # IMPORTANT: update AFTER processing i
            suf_min = min(suf_min, nums[i])

        return ans