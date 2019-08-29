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

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        count = 0
        lst = list(s)
        state = True
        valid = [True] * len(s)
        while state:
            state = False
            for i in range(len(lst)-1):
                if valid[i] == True and (lst[i], lst[i+1]) == ('(', ')'):
                    count += 2
                    valid[i] = valid[i+1] = False
                    state = True
        return count


s = Solution()
assert (s.longestValidParentheses('()()')) == 4
assert (s.longestValidParentheses('(')) == 0
assert (s.longestValidParentheses(')(')) == 0
assert (s.longestValidParentheses('()')) == 2
assert (s.longestValidParentheses(')()')) == 2
assert (s.longestValidParentheses('(()')) == 2
assert (s.longestValidParentheses('(()(((()')) == 2
assert (s.longestValidParentheses(')()())')) == 4
assert (s.longestValidParentheses('()(()')) == 2
assert (s.longestValidParentheses('()(())')) == 6
