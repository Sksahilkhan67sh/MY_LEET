class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:

        def waviness(x):
            digits = str(x)

            if len(digits) < 3:
                return 0

            count = 0

            for i in range(1, len(digits) - 1):
                if (
                    digits[i] > digits[i - 1]
                    and digits[i] > digits[i + 1]
                ) or (
                    digits[i] < digits[i - 1]
                    and digits[i] < digits[i + 1]
                ):
                    count += 1

            return count

        ans = 0

        for x in range(num1, num2 + 1):
            ans += waviness(x)

        return ans