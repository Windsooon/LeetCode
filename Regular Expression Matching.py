class Solution(object):
    def isMatch(self, s, p):
        s = ' ' + s
        p = ' ' + p
        lst = [True] + [False] * (len(p)-1)
        for l in range(2, len(lst)):
            if p[l] == '*' and lst[l-2]:
                lst[l] = True
        # ' a*.*b' [True, False, True, False, True, False]
        old = lst[:]
        for i in range(1, len(s)):
            for j in range(len(p)):
                if p[j] == '*':
                    lst[j] = lst[j-1] or lst[j-2] or (lst[j] and (s[i] == s[i-1] or p[j-1] == '.'))
                else:
                    lst[j] = (s[i] == p[j] or p[j] == '.') and old[j-1]
            old = lst[:]
        return lst[-1]


s = Solution()
s.isMatch('abcdb', 'a*.*b')
