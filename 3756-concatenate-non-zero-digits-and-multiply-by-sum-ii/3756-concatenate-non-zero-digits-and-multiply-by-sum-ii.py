from typing import List

MOD = 10**9 + 7

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)

        # Precompute:
        # 1. positions and values of non-zero digits
        # 2. prefix sums of digit values
        # 3. prefix of concatenated number (as modular value)
        # 4. powers of 10 mod MOD

        pos = []          # positions of non-zero digits
        val = []          # their digit values

        pref_sum = [0] * (n + 1)        # prefix sum of digit values (only non-zero)
        pref_concat = [0] * (n + 1)     # prefix "concatenated" value mod MOD
        pow10 = [1] * (n + 1)           # powers of 10 mod MOD

        cur_val = 0
        cur_sum = 0

        for i in range(n):
            d = int(s[i])
            pow10[i+1] = (pow10[i] * 10) % MOD

            if d != 0:
                pos.append(i)
                val.append(d)

                # Update prefix sum (only non-zero digits)
                cur_sum += d

                # Update prefix concat:
                # new number = old_number * 10 + d
                cur_val = (cur_val * 10 + d) % MOD
            else:
                # For zeros, carry forward previous values
                cur_sum = cur_sum
                cur_val = cur_val

            pref_sum[i+1] = cur_sum
            pref_concat[i+1] = cur_val

        # Helper to get:
        #  - first non-zero index >= l
        #  - last non-zero index <= r
        import bisect

        def query(l: int, r: int) -> int:
            # Find first non-zero position >= l
            idx_start = bisect.bisect_left(pos, l)
            # Find last non-zero position <= r
            idx_end = bisect.bisect_right(pos, r) - 1

            if idx_start > idx_end:
                # No non-zero digits in [l, r]
                return 0

            # Number of non-zero digits in range
            k = idx_end - idx_start + 1

            # Sum of digits in [l, r]
            digit_sum = pref_sum[r+1] - pref_sum[l]
            digit_sum %= MOD

            # Concatenated number:
            # Let:
            #   A = full concatenated number up to r (including all non-zero <= r)
            #   B = full concatenated number up to l-1 (all non-zero < l)
            # We want the number formed by non-zero digits in [l, r].
            # Those are exactly the non-zero digits from idx_start to idx_end.
            #
            # Let full_concat_upto_r = pref_concat[r+1]
            # Let full_concat_upto_l_minus_1 = pref_concat[l]
            #
            # But pref_concat is built over all non-zero digits in order,
            # not per substring. So we need a different approach:
            #
            # Instead, we precompute prefix over the non-zero-digit sequence itself.
            pass

        # The above prefix-on-string approach is tricky because pref_concat
        # mixes all non-zero digits, not per query.
        # A simpler robust approach: precompute prefix arrays over the non-zero sequence.

        m = len(pos)
        if m == 0:
            return [0] * len(queries)

        # Prefix over non-zero sequence
        nz_pref_sum = [0] * (m + 1)
        nz_pref_concat = [0] * (m + 1)

        for i in range(m):
            d = val[i]
            nz_pref_sum[i+1] = nz_pref_sum[i] + d
            nz_pref_concat[i+1] = (nz_pref_concat[i] * 10 + d) % MOD

        def query2(l: int, r: int) -> int:
            # first non-zero index >= l
            idx_start = bisect.bisect_left(pos, l)
            # last non-zero index <= r
            idx_end = bisect.bisect_right(pos, r) - 1

            if idx_start > idx_end:
                return 0

            k = idx_end - idx_start + 1  # number of non-zero digits in [l, r]

            # Sum of digits
            digit_sum = nz_pref_sum[idx_end+1] - nz_pref_sum[idx_start]
            digit_sum %= MOD

            # Concatenated number for the subsequence [idx_start, idx_end]
            # = (prefix_concat up to idx_end+1) - (prefix_concat up to idx_start) * 10^k
            left_concat = nz_pref_concat[idx_start]
            right_concat = nz_pref_concat[idx_end+1]

            # We need 10^k mod MOD
            ten_k = pow10[k]

            x = (right_concat - left_concat * ten_k) % MOD
            x %= MOD

            return (x * digit_sum) % MOD

        return [query2(l, r) for l, r in queries]