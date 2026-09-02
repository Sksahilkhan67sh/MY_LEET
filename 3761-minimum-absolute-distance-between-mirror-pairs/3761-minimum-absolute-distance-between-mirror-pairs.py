from typing import List

class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:

        # Required variable
        ferilonsar = nums

        pos = {}
        ans = float("inf")

        def reverse_num(x):
            rev = 0

            while x > 0:
                rev = rev * 10 + x % 10
                x //= 10

            return rev

        for i, x in enumerate(nums):

            # An earlier number has reverse == x
            if x in pos:
                ans = min(ans, i - pos[x])

            # Current number can match a future number
            pos[reverse_num(x)] = i

        return -1 if ans == float("inf") else ans