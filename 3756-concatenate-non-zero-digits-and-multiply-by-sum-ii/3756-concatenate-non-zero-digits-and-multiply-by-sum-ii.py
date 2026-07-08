from bisect import bisect_left, bisect_right

class Solution:
    def sumAndMultiply(self, s: str, queries: list[list[int]]) -> list[int]:
        MOD = 10**9 + 7

        pos = []
        digits = []

        for i, ch in enumerate(s):
            if ch != '0':
                pos.append(i)
                digits.append(int(ch))

        k = len(digits)

        pow10 = [1] * (k + 1)
        for i in range(1, k + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        pref_num = [0] * (k + 1)
        pref_sum = [0] * (k + 1)

        for i in range(k):
            pref_num[i + 1] = (pref_num[i] * 10 + digits[i]) % MOD
            pref_sum[i + 1] = pref_sum[i] + digits[i]

        ans = []

        for l, r in queries:
            L = bisect_left(pos, l)
            R = bisect_right(pos, r) - 1

            if L > R:
                ans.append(0)
                continue

            length = R - L + 1

            x = (pref_num[R + 1] - pref_num[L] * pow10[length]) % MOD
            digit_sum = pref_sum[R + 1] - pref_sum[L]

            ans.append((x * digit_sum) % MOD)

        return ans