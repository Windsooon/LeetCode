class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s = ' ' + s
        p = ' ' + p
        lst = [False] * len(p)
        lst[0] = True
        # a*c?b
        # [True, False, False, False, False, False]
        for i in range(1, len(lst)):
            # ' **ab' -> [True, True, True, False, False]
            if p[i] == '*' and lst[i-1]:
                lst[i] = True
        old = lst[:]
        for i in range(1, len(s)):
            for j in range(len(p)):
                if p[j] == '*':
                    lst[j] = lst[j-1] or lst[j]
                else:
                    lst[j] = old[j-1] and (p[j] == s[i] or p[j] == '?')
            old = lst[:]
        return lst[-1]


class Solution:
    def isMatch(self, s, p):
        nfa, accept = self.builddfa(p)
        state = set([0])
        # a*b?c
        for char in s:
            new = set()
            for s in state:
                for t in [char, '*', '?']:
                    new.add(nfa.get((s, t)))
            state = new
        return accept in state

    def builddfa(self, p):
        res = {}
        current = 0
        for i in range(len(p)):
            # a*b?c
            # 0, a -> 1
            # 1 * = 2
            if p[i] == '*':
                res[(current, '*')] = current
            else:
                res[(current, p[i])] = current + 1
                current += 1
        accept = current
        return res, accept





s = Solution()
assert s.isMatch('adcec', 'a*c?c') is True
assert s.isMatch('acdcb', 'a*c?b') is False
assert s.isMatch('adceb', '*a*b') is True
assert s.isMatch('adceb', '*a*') is True
assert s.isMatch('cd', '?a') is False
assert s.isMatch('aa', '*') is True
assert s.isMatch('aa', 'a') is False
assert s.isMatch('a', '') is False
assert s.isMatch('aab', 'c*a*b') is False
assert s.isMatch('ho', '**ho') is True
