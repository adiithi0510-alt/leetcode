class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        last = {'a': -1, 'b': -1, 'c': -1}
        count = 0
        for i, ch in enumerate(s):
            last[ch] = i
            count += min(last['a'], last['b'], last['c']) + 1
        return count