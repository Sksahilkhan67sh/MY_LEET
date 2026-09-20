from typing import List

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        target_index = 0

        for num in range(1, n + 1):
            ans.append("Push")

            if num == target[target_index]:
                target_index += 1

                if target_index == len(target):
                    break
            else:
                ans.append("Pop")

        return ans