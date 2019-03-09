class Solution(object):
    def isMatch(self, s, p):
        s = ' ' + s
        p = ' ' + p
        lst = [False] * len(p)
        lst[0] = True
        for l in range(2, len(p)):
            lst[l] = True if lst[l-2] and p[l] == '*' else False
        old = lst[:]
        # [True False]
        for i in range(1, len(s)):
            # breakpoint()
            for j in range(len(p)):
                if j == 0:
                    lst[j] = False
                else:
                    if p[j] == '*':
                            lst[j] = (
                                lst[j-2] or
                                lst[j-1] or
                                ((s[i] == s[i-1] or p[j-1] == '.') and lst[j]))
                    else:
                        lst[j] = old[j-1] and (p[j] == s[i] or p[j] == '.')
            old = lst[:]
        return lst[-1]


s = Solution()
assert s.isMatch('ab', '.*..') is True
assert s.isMatch('aaa', 'a') is False
assert s.isMatch('mississippi', 'mis*is*p*.') is False
assert s.isMatch('ab', '.*') is True
assert s.isMatch('', '.*') is True
assert s.isMatch('aab', 'c*a*b') is True
assert s.isMatch('', '') is True
assert s.isMatch('b', 'ba*') is True
assert s.isMatch('ba', 'ba*') is True
assert s.isMatch('baa', 'ba*') is True
assert s.isMatch('a', '') is False
assert s.isMatch('abc', 'a.c') is True
assert s.isMatch('aa', 'a') is False
assert s.isMatch('aa', 'a*') is True
assert s.isMatch('cab', 'c.*') is True
assert s.isMatch('abc', 'a.c') is True
assert s.isMatch('aaa', 'ab*ac*a') is True
