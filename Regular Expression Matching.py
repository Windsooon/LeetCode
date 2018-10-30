classfi nfi nfin Solution(object):
    def isMatch(self, s, p):
        matrix = [[False] * (len(p)+1) for _ in range(len(s)+1)]
        matrix[0][0] = True
        for i in range(2, len(p)+1):
            matrix[0][i] = matrix[0][i-2] and p[i-1] == '*'

        for s_i in range(len(s)+1):
            for p_i in range(len(p)+1):
                if p_v == '.' or p_v == s_v:
                elif p_v == '*':
        return matrix[-1][-1]


s = Solution()
assert s.isMatch('a', '') is False
assert s.isMatch('abc', 'a.c') is True
assert s.isMatch('aa', 'a') is False
assert s.isMatch('aa', 'a*') is True
assert s.isMatch('ab', '.*') is True
assert s.isMatch('abc', 'a.c') is True
# s.isMatch('aab', 'c*a*b')
assert s.isMatch('aab', 'c*a*b') is True
assert s.isMatch('aaa', 'ab*ac*a') is True
