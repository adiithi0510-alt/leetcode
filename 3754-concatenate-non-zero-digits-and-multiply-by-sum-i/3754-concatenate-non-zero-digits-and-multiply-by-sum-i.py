class Solution:
    def sumAndMultiply(self, n: int) -> int:
        digits = []

        for ch in str(n):
            if ch != '0':
                digits.append(ch)

        if not digits:
            return 0

        x = int("".join(digits))
        digit_sum = sum(int(d) for d in digits)

        return x * digit_sum
        