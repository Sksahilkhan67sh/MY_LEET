from typing import List

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        nums = set()

        n = len(digits)

        for i in range(n):
            # Units digit must be even
            if digits[i] % 2 != 0:
                continue

            for j in range(n):
                if j == i:
                    continue

                for k in range(n):
                    if k == i or k == j:
                        continue

                    # Hundreds digit cannot be zero
                    if digits[k] == 0:
                        continue

                    number = digits[k] * 100 + digits[j] * 10 + digits[i]
                    nums.add(number)

        return len(nums)