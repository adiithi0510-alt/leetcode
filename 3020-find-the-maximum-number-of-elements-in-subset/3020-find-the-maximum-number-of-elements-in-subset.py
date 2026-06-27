class Solution:
    def maximumLength(self, nums):
        from collections import Counter
        
        count = Counter(nums)
        max_len = 1
        
        for x in count:
            if x == 1:
                c = count[1]
                max_len = max(max_len, c if c % 2 == 1 else c - 1)
                continue
            
            length = 0
            curr = x
            
            while curr in count and count[curr] >= 2:
                length += 2
                curr = curr * curr
                if curr > 10**9:
                    curr = -1  # sentinel
                    break
            
            # curr is the candidate center
            if curr in count:
                length += 1  # valid: has a center
            elif length >= 2:
                # pairs exist but no center found — invalid pattern, 
                # so best we can do is shorten by removing outermost pair
                # and use previous curr as center
                length -= 1  # remove one from pair to make it a center
            else:
                length = 1  # just x itself as a single element
            
            max_len = max(max_len, length)
        
        return max_len