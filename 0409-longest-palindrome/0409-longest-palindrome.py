class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import Counter
        count = Counter(s)
        
        length = 0
        odd = False
        
        for c in count.values():
            if c % 2 == 0:
                length += c
            else:
                length += c - 1
                odd = True
        
        return length + 1 if odd else length
        