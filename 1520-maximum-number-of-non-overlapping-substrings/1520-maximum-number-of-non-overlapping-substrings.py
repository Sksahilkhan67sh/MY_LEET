from typing import List

class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        n = len(s)

        first = [n] * 26
        last = [-1] * 26

        # First and last occurrence of every character
        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')
            first[idx] = min(first[idx], i)
            last[idx] = i

        intervals = []

        # Build the smallest valid interval starting
        # from the first occurrence of each character.
        for c in range(26):
            if first[c] == n:
                continue

            left = first[c]
            right = last[c]
            i = left
            valid = True

            while i <= right:
                idx = ord(s[i]) - ord('a')

                # This character appeared before our left boundary,
                # so this interval cannot be valid.
                if first[idx] < left:
                    valid = False
                    break

                right = max(right, last[idx])
                i += 1

            if valid:
                intervals.append((right, left))

        # Earliest ending interval first
        intervals.sort()

        ans = []
        prev_end = -1

        for right, left in intervals:
            if left > prev_end:
                ans.append(s[left:right + 1])
                prev_end = right

        return ans