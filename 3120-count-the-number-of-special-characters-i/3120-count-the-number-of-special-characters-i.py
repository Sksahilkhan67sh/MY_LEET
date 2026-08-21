class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        chars = set(word)

        ans = 0

        for i in range(26):
            lower = chr(ord('a') + i)
            upper = chr(ord('A') + i)

            if lower in chars and upper in chars:
                ans += 1

        return ans