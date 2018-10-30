class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for t in tokens:
            if t in ('+', '-', '*', '/'):
                second = int(stack.pop())
                first = int(stack.pop())
                if t == '+':
                    stack.append(first+second)
                elif t == '-':
                    stack.append(first-second)
                elif t == '*':
                    stack.append(first*second)
                else:
                    stack.append(int(first/second))
            else:
                stack.append(t)
        return int(stack[-1])

s = Solution()
assert s.evalRPN(["2", "1", "+", "3", "*"]) == 9
assert s.evalRPN(["4", "13", "5", "/", "+"]) == 6
assert s.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22
