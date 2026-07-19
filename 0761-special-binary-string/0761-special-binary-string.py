class Solution:
    def makeLargestSpecial(self, s: str) -> str:

        if len(s) <= 2:
            return s

        parts = []
        balance = 0
        start = 0

        for i, ch in enumerate(s):

            if ch == '1':
                balance += 1
            else:
                balance -= 1

            if balance == 0:
                middle = self.makeLargestSpecial(s[start + 1:i])
                parts.append("1" + middle + "0")
                start = i + 1

        parts.sort(reverse=True)

        return "".join(parts)