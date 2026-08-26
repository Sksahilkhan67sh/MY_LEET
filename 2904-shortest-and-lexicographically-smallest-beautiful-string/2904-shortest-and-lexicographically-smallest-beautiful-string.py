class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        left = 0
        ones = 0
        ans = ""

        for right in range(len(s)):
            if s[right] == '1':
                ones += 1

            # Too many 1s
            while ones > k:
                if s[left] == '1':
                    ones -= 1
                left += 1

            # Remove unnecessary leading zeros
            while left < right and s[left] == '0':
                left += 1

            # Exactly k ones
            if ones == k:
                cur = s[left:right + 1]

                if (
                    ans == ""
                    or len(cur) < len(ans)
                    or (len(cur) == len(ans) and cur < ans)
                ):
                    ans = cur

        return ans