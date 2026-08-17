from typing import List
from functools import cache
from itertools import accumulate


class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        prefix = list(accumulate(stoneValue, initial=0))

        @cache
        def dfs(left: int, right: int) -> int:
            if left >= right:
                return 0

            ans = 0
            left_sum = 0
            right_sum = prefix[right + 1] - prefix[left]

            for k in range(left, right):
                left_sum += stoneValue[k]
                right_sum -= stoneValue[k]

                if left_sum < right_sum:
                    # Bob keeps the right side and throws left away.
                    # Alice gets left side.
                    if ans >= 2 * left_sum:
                        continue

                    ans = max(
                        ans,
                        left_sum + dfs(left, k)
                    )

                elif left_sum > right_sum:
                    # Alice gets right side.
                    if ans >= 2 * right_sum:
                        break

                    ans = max(
                        ans,
                        right_sum + dfs(k + 1, right)
                    )

                else:
                    # Equal sums: Alice can choose either side.
                    ans = max(
                        ans,
                        left_sum + dfs(left, k),
                        right_sum + dfs(k + 1, right)
                    )

            return ans

        return dfs(0, len(stoneValue) - 1)