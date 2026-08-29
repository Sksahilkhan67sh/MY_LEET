from typing import List

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixes = set()

        # Store every prefix of every number in arr1
        for num in arr1:
            while num > 0:
                prefixes.add(num)
                num //= 10

        ans = 0

        # Check prefixes of numbers in arr2
        for num in arr2:
            x = num

            while x > 0:
                if x in prefixes:
                    ans = max(ans, len(str(x)))
                    break

                x //= 10

        return ans