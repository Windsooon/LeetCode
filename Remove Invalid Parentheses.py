from queue import Queue
class Solution:
    def removeInvalidParentheses(self, s):
        self.q = Queue()
        self.visit = {}
        if not s:
            return [""]
        self.res = []
        self.q.put(s)
        self.bfs()
        return self.res if self.res else [""]

    def bfs(self):
        # base case
        while 1:
            if self.q.empty():
                return
            val = self.q.get()
            if val in self.visit:
                continue
            self.visit[val] = True
            if self.isValid(val):
                self.res.append(val)
                return
            if len(val) == 1:
                return
            for i in range(len(val)+1):
                string = val[:i]+val[i+1:]
                if string:
                    self.q.put(string)
                    if self.isValid(string):
                        if string not in self.res:
                            print(val)
                            self.res.append(string)
            if self.res:
                return
        return


    def isValid(self, tem):
        left = right = 0
        for t in tem:
            if t == '(':
                left += 1
            elif t == ')':
                right += 1
            if right > left:
                return False
        return left == right


s = Solution()
# assert s.removeInvalidParentheses('n') == ['n']
# assert s.removeInvalidParentheses('nn') == ['nn']
# assert s.removeInvalidParentheses('n)(') == ['n']
# assert s.removeInvalidParentheses('(n)') == ['(n)']
# assert s.removeInvalidParentheses('()())()') == ['(())()', '()()()']
# assert s.removeInvalidParentheses('(a)())()') == ["(a())()", "(a)()()"]
# assert s.removeInvalidParentheses(')(') == [""]
# assert s.removeInvalidParentheses('()(j))(') == ["((j))"]
# assert s.removeInvalidParentheses(")((((((((") == [""]
print(s.removeInvalidParentheses("(k()("))
