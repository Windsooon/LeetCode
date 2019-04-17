class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # ()(())
        stack = [-1]
        result = 0
        for i in range(len(s)):
            if s[i] == ')' and len(stack) > 1 and s[stack[-1]] == '(':
                stack.pop()
                result = max(result, i-stack[-1])
            else:
                stack.append(i)
        return result


s = Solution()
assert (s.longestValidParentheses('(')) == 0
assert (s.longestValidParentheses(')(')) == 0
assert (s.longestValidParentheses('()')) == 2
assert (s.longestValidParentheses('()()')) == 4
assert (s.longestValidParentheses(')()')) == 2
assert (s.longestValidParentheses('(()')) == 2
assert (s.longestValidParentheses('(()(((()')) == 2
assert (s.longestValidParentheses(')()())')) == 4
assert (s.longestValidParentheses('()(()')) == 2
assert (s.longestValidParentheses('()(())')) == 6
