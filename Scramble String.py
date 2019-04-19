class Solution:
    def __init__(self):
        self.dic = {}

    def isScramble(self, s1, s2):
        if (s1, s2) in self.dic:
            return self.dic[(s1, s2)]
        if sorted(s1) != sorted(s2):
            self.dic[(s1, s2)] = False
            return False
        if s1 == s2:
            self.dic[(s1, s2)] = True
            return True
        for i in range(1, len(s1)):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]) or \
                    self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i]):
                return True
        return False

s = Solution()
assert s.isScramble('great', 'rgeat') is True
assert s.isScramble('great', 'rgtae') is True
assert s.isScramble('abcde', 'caebd') is False
assert s.isScramble('abc', 'bca') is True
