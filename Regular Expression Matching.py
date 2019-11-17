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

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        self.cache = dict()
        return self.recurison(s, p)
    
    def recurison(self, s, p):
        if (s, p) in self.cache:
            return self.cache[(s, p)]
        if not s and not p:
            return True
        if not p:
            return False
        if not s:
            if len(p) > 1 and p[1] == '*':
                ans = self.isMatch(s, p[2:])
                self.cache[(s, p)] = ans
                return ans
            else:
                return False
        if s[0] == p[0] or p[0] == '.':
            if len(p) > 1 and p[1] == '*':
                first = self.isMatch(s[1:], p[2:])
                self.cache[(s[1:], p[2:])] = first
                second = self.isMatch(s[1:], p)
                self.cache[(s[1:], p)] = second
                third = self.isMatch(s, p[2:])
                self.cache[(s, p[2:])] = third
                ans = first or second or third
                self.cache[(s, p)] = ans
                return ans
            else:
                ans = self.isMatch(s[1:], p[1:])
                self.cache[(s, p)] = ans
                return ans
        ans = self.isMatch(s, p[2:])
        self.cache[(s, p)] = ans
        return ans

s = Solution()
# assert s.isMatch('aa', 'a') is False
# assert s.isMatch('aa', 'a*') is True
# assert s.isMatch('ab', '.*') is True
soo = "aaaaaaaaaaaaab"
p = "a*a*a*a*a*a*a*a*a*a*c"
print(s.isMatch(soo, p))
# assert s.isMatch('aa', 'c*a*') is True
# assert s.isMatch('mississippi', 'mis*is*p*.') is False
# assert s.isMatch('abcdb', 'a*.*b') is True
