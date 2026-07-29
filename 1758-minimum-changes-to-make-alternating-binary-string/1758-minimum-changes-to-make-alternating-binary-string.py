class Solution:
    def minOperations(self, s: str) -> int:
        mismatch = 0

        for i, ch in enumerate(s):
            expected = str(i % 2)      # Pattern: 010101...
            if ch != expected:
                mismatch += 1

        return min(mismatch, len(s) - mismatch)