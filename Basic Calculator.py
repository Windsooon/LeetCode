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



s = Solution()
# print(s.calculate('1 + 1'))
# print(s.calculate('2-1 + 2'))
# print(s.calculate("(1+(4+5+2)-3)+(6+8)"))
# print(s.calculate("11+22-33+15-111"))
# print(s.calculate("0"))
# print(s.calculate("100"))
# print(s.calculate("4-5+2"))
print(s.calculate("(4+5+2)"))
