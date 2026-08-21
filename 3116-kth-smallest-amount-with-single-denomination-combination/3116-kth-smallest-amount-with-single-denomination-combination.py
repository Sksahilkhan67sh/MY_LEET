from typing import List
from math import gcd


class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)

        
        subsets = []

        for mask in range(1, 1 << n):
            lcm = 1
            bits = 0

            for i in range(n):
                if mask & (1 << i):
                    bits += 1
                    lcm = lcm * coins[i] // gcd(lcm, coins[i])

            subsets.append((lcm, bits))

        def count(x: int) -> int:
            """Number of distinct valid amounts <= x."""
            total = 0

            for lcm, bits in subsets:
                if lcm > x:
                    continue

                if bits & 1:
                    total += x // lcm
                else:
                    total -= x // lcm

            return total

        # The kth answer cannot exceed k * minimum coin.
        left = 1
        right = min(coins) * k

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left