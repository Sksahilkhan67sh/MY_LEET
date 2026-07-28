from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        freq = Counter(s)

        left = []
        middle = ""

        for i in range(26):
            ch = chr(ord('a') + i)
            left.append(ch * (freq[ch] // 2))
            if freq[ch] % 2:
                middle = ch

        left = "".join(left)
        return left + middle + left[::-1]