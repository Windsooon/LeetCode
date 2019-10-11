class Solution:
    def removeInvalidParentheses(self, s: str):
        current = []
        current.append(s)
        ans = []
        visited = set()
        while current:
            tem = []
            for top in current:
                if self.isValid(s):
                    return [s]
                for i in range(len(top)):
                    if top[:i]+top[i+1:] not in visited:
                        visited.add(top[:i]+top[i+1:])
                        if self.isValid(top[:i]+top[i+1:]) and top[:i]+top[i+1:] not in ans:
                            ans.append(top[:i]+top[i+1:])
                        tem.append(top[:i]+top[i+1:])
            if not ans:
                current = tem
            else:
                return ans

    def isValid(self, s):
        count = 0
        for i in range(len(s)):
            if s[i] == '(':
                count += 1
            elif s[i] == ')':
                count -= 1
                if count < 0:
                    return False
        return count == 0

s = Solution()

assert s.removeInvalidParentheses('n') == ['n']
assert s.removeInvalidParentheses('nn') == ['nn']
assert s.removeInvalidParentheses('n)(') == ['n']
assert s.removeInvalidParentheses('(n)') == ['(n)']
assert s.removeInvalidParentheses('()())()') == ['(())()', '()()()']
assert s.removeInvalidParentheses('(a)())()') == ["(a())()", "(a)()()"]
assert s.removeInvalidParentheses(')(') == [""]
assert s.removeInvalidParentheses(")((((((((") == [""]
# (s.removeInvalidParentheses("(k()("))
assert s.removeInvalidParentheses("(((k()((") == ["k()","(k)"]
print(s.removeInvalidParentheses("()(((((((()"))
