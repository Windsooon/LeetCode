class Solution:
    def calculate(self, s):
        res, num, sign, stack = 0, 0, 1, []
        for ss in s:
            if ss.isdigit():
                num = 10*num + int(ss)
            elif ss in ["-", "+"]:
                res += sign*num
                num = 0
                sign = [-1, 1][ss=="+"]
            elif ss == "(":
                stack.append(res)
                stack.append(sign)
                sign, res = 1, 0
            elif ss == ")":
                res += sign*num
                res *= stack.pop()
                res += stack.pop()
                num = 0
        return res + num*sign

class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0
        res, stack = [0], []
        # (1 + (4 + 5))
        s = '(' + s + ')'
        for i in range(len(s)):
            if s[i] == ' ':
                continue
            elif s[i].isdigit():
                if s[i-1].isdigit() or stack == [0]:
                    res[-1] = res[-1] * 10 + int(s[i])
                else:
                    res.append(int(s[i]))
            elif s[i] == '(':
                stack.append('(')
            elif s[i] == ')':
                while 1:
                    top = stack.pop()
                    if top == '(':
                        break
                    else:
                        second = res.pop()
                        first = res.pop()
                        res.append(self.cal(first, top, second))
            elif s[i] in '+-':
                while stack and stack[-1] in '+-':
                    top = stack.pop()
                    second = res.pop()
                    first = res.pop()
                    res.append(self.cal(first, top, second))
                stack.append(s[i])
        return res[-1]

    def cal(self, first, operator, second):
        if operator == '+':
            return first + second
        else:
            return first - second

s = Solution()
print(s.calculate("(1+(4+5))"))
print(s.calculate("0+0"))
# print(s.calculate('1 + 1'))
# print(s.calculate('2-1 + 2'))
# print(s.calculate("(1+(4+5+2)-3)+(6+8)"))
# print(s.calculate("11+22-33+15-111"))
# print(s.calculate("0"))
# print(s.calculate("100"))
# print(s.calculate("4-5+2"))
# print(s.calculate("(4+5+2)"))
