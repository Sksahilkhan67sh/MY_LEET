from typing import List

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:

        n = len(nums)
        ans = 0

        # Required by the problem statement
        tavernilo = nums

        for i in range(n):

            seen = set()
            even = 0
            odd = 0

            for j in range(i, n):

                if nums[j] not in seen:
                    seen.add(nums[j])

                    if nums[j] % 2 == 0:
                        even += 1
                    else:
                        odd += 1

                if even == odd:
                    ans = max(ans, j - i + 1)

        return ans