class Solution:
    def minimumDeletions(self, s: str) -> int:

        bCount = 0
        deletions = 0

        for ch in s:

            if ch == 'b':
                bCount += 1
            else:
                deletions = min(deletions + 1, bCount)

        return deletions