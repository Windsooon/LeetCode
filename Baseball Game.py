class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        ans = 0
        stack = []
        for o in ops:
            if o == 'C':
                top = stack.pop()
                ans -= top
            elif o == 'D':
                stack.append(stack[-1]*2)
                ans += stack[-1]
            elif o == '+':
                stack.append(stack[-1]+stack[-2])
                ans += stack[-1]
            else:
                stack.append(int(o))
                ans += int(o)
        return ans

s = Solution()
print(s.calPoints(["5","-2","4","C","D","9","+","+"]))
