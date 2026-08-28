class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)

        # Required variable from the problem statement.
        calendrix = (s, target)

        # Count characters.
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - 97] += 1

        # A palindrome can have at most one odd frequency.
        odd = 0
        mid = ""

        for i in range(26):
            if cnt[i] % 2:
                odd += 1
                mid = chr(i + 97)

        if odd > 1:
            return ""

        # Counts for the left half.
        half = [x // 2 for x in cnt]
        half_len = n // 2

        # Build the left half.
        left = []

        for pos in range(half_len):
            target_char = ord(target[pos]) - 97

            # Try the smallest possible character.
            for c in range(26):
                if half[c] == 0:
                    continue

                # If we choose a character smaller than target[pos],
                # the final palindrome can never become greater.
                if c < target_char:
                    continue

                # If we choose a character greater than target[pos],
                # the remaining part can be minimized freely.
                if c > target_char:
                    half[c] -= 1

                    suffix = []
                    for x in range(26):
                        suffix.append(chr(x + 97) * half[x])

                    left_str = "".join(left) + chr(c + 97) + "".join(suffix)

                    right_str = left_str[::-1]

                    ans = left_str + mid + right_str

                    return ans if ans > target else ""

                # c == target_char.
                # We can use it only if the prefix can remain equal.
                half[c] -= 1

                # Check whether the largest possible completion
                # can still beat target.
                suffix = []

                for x in range(25, -1, -1):
                    suffix.append(chr(x + 97) * half[x])

                max_left = "".join(left) + chr(c + 97) + "".join(suffix)
                max_pal = max_left + mid + max_left[::-1]

                if max_pal > target:
                    left.append(chr(c + 97))
                    break

                # This character cannot lead to a valid answer.
                half[c] += 1

            else:
                # No possible character at this position.
                return ""

        # We matched target's left half.
        left_str = "".join(left)
        ans = left_str + mid + left_str[::-1]

        if ans > target:
            return ans

        return ""