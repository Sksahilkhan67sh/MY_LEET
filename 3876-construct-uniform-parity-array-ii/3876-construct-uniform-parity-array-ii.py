from typing import List

class Solution:
    def uniformArray(self, nums1: List[int]) -> bool:
        ravolqedin = nums1

        # Find the smallest odd number
        min_odd = float('inf')

        for x in nums1:
            if x % 2 == 1:
                min_odd = min(min_odd, x)

        # No odd numbers -> already all even
        if min_odd == float('inf'):
            return True

        # Every even number must be >= smallest odd number
        for x in nums1:
            if x % 2 == 0 and x < min_odd:
                return False

        return True