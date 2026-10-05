class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        depth = 0
        ans = 0

        for i, ch in enumerate(s):
            if ch == '(':
                depth += 1
            else:
                depth -= 1

                # "()" -> 2^depth
                if s[i - 1] == '(':
                    ans += 1 << depth

        return ans