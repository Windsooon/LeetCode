class Solution:
    def diffWaysToCompute(self, input):
        return self.recursion(input)

    def recursion(self, input):
        """
        append all valid answer to self.ans with recursion
        >>> recursion('2-1-1')
        >>> self.ans == [0, 2]
        >>> True
        """
        if input.isdigit():
            return [int(input)]
        ans = []
        for i in range(len(input)):
            if input[i] in ('+', '-', '*'):
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i+1:])
                for l in left:
                    for r in right:
                        tem = self.helper(l, r, input[i])
                        ans.append(tem)
        return ans


    def helper(self, left, right, oper):
        if oper == '+':
            return left + right
        elif oper == '-':
            return left - right
        else:
            return left * right

s = Solution()
print(s.diffWaysToCompute("2*3-4*5"))
