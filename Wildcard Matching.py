




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

class Solution:
    def isMatch(self, s, p):
        self.visited = dict()
        self.count = 0
        ans = self.match(s, p)
        print(self.count)
        return ans

    def match(self, s, p):
        self.count += 1
        if (s, p) in self.visited:
            breakpoint()
            return self.visited[(s, p)]
        if not s and not p:
            self.visited[(s, p)] = True
            return True
        if not s:
            if len(set(p)) == 1 and p[0] == '*':
                self.visited[(s, p)] = True
                return True
            else:
                self.visited[(s, p)] = False
                return False
        if not p:
            self.visited[(s, p)] = False
            return False
        if p[0] == '*':
            boolean = self.match(s[1:], p) or self.match(s, p[1:])
        else:
            if s[0] == p[0] or p[0] == '?':
                boolean = self.match(s[1:], p[1:])
            else:
                self.visited[(s, p)] = False
                return False
        self.visited[(s, p)] = boolean
        return boolean



s = Solution()
# assert s.isMatch('', '*') is True
# assert s.isMatch('ho', 'ho**') is True
# assert s.isMatch('adcec', 'a*c?c') is True
# assert s.isMatch('acdcb', 'a*c?b') is False
# assert s.isMatch('adceb', '*a*b') is True
# assert s.isMatch('adceb', '*a*') is True
# assert s.isMatch('cd', '?a') is False
# assert s.isMatch('aa', '*') is True
# assert s.isMatch('aa', 'a') is False
# assert s.isMatch('a', '') is False
# assert s.isMatch('aab', 'c*a*b') is False
# assert s.isMatch('ho', '**ho') is True
assert s.isMatch('ab', '***ab') is True
# assert s.isMatch('aaabababaaabaababbbaaaabbbbbbabbbbabbbabbaabbababab', '*ab***ba**b*b*aaab*b') is True
