class Solution(object):
    def isIsomorphic(self, s, t):
        # foo bar
        d1, d2 = [0 for _ in range(256)], [0 for _ in range(256)]
        for i in range(len(s)):
            if d1[ord(s[i])] != d2[ord(t[i])]:
                return False
            d1[ord(s[i])] = i+1
            d2[ord(t[i])] = i+1
        return True

s = Solution()
print(s.isIsomorphic3('foo', 'baa'))
