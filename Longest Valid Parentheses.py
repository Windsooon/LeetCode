class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1:
            return 0
        s += 'x'
        max_len = 0
        stack = []
        for k, v in enumerate(s):
            if v == ')' and stack and s[stack[-1]] == '(':
                stack.pop()
            else:
                if not stack:
                    max_len = max(max_len, k)
                else:
                    max_len = max(max_len, k-stack[-1]-1)
                stack.append(k)
        if not stack:
            return len(stack)
        else:
            return max_len


s = Solution()
print(s.longestValidParentheses('('))
print(s.longestValidParentheses(')('))
print(s.longestValidParentheses(')()'))
print(s.longestValidParentheses('(()'))
print(s.longestValidParentheses(')()())'))
print(s.longestValidParentheses('()(()'))
