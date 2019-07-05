from functools import reduce

class Solution:
    def longestDupSubstring(self, S):
        self.ans = ''
        mod = 2**63 - 1

        def test(L):
            seen = set()
            for i in range(len(S)-L+1):
                if hash(S[i:i+L]) % mod in seen:
                    self.ans = S[i:i+L]
                    return True
                else:
                    seen.add(hash(S[i:i+L]) % mod)
            return False
        res, lo, hi = 0, 0, len(S)
        while lo < hi:
            mi = (lo + hi + 1) // 2
            pos = test(mi)
            if pos:
                lo = mi
            else:
                hi = mi - 1
        return self.ans

    
s = Solution()
string = "banana"
print(s.longestDupSubstring(string))
