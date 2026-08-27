class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)

        # Frequency of characters in s
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        # We try to keep target's prefix as long as possible.
        # If we can make a bigger character at position i,
        # the suffix should be sorted as small as possible.
        for i in range(n - 1, -1, -1):

            # We need the characters target[0:i].
            # Rebuild the remaining frequency for this prefix.
            remaining = cnt[:]

            possible = True

            for j in range(i):
                x = ord(target[j]) - ord('a')

                if remaining[x] == 0:
                    possible = False
                    break

                remaining[x] -= 1

            if not possible:
                continue

            # Find the smallest character strictly greater
            # than target[i].
            x = ord(target[i]) - ord('a')

            for c in range(x + 1, 26):
                if remaining[c] > 0:

                    remaining[c] -= 1

                    # Put the smallest possible characters
                    # in the remaining positions.
                    ans = target[:i] + chr(c + ord('a'))

                    for d in range(26):
                        ans += chr(d + ord('a')) * remaining[d]

                    return ans

        return ""