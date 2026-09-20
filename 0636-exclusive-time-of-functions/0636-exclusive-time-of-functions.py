from typing import List

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ans = [0] * n
        stack = []
        prev_time = 0

        for log in logs:
            func_id, action, timestamp = log.split(":")
            func_id = int(func_id)
            timestamp = int(timestamp)

            if action == "start":
                # Current function was running before this new function started
                if stack:
                    ans[stack[-1]] += timestamp - prev_time

                stack.append(func_id)
                prev_time = timestamp

            else:
                # Current function runs through timestamp
                ans[stack.pop()] += timestamp - prev_time + 1

                # Next execution starts after this timestamp
                prev_time = timestamp + 1

        return ans