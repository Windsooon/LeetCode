class Solution:
    def removeKdigits(self, num, k):
        stack = []
        for d in num:
            while k and stack and stack[-1] > d:
                stack.pop()
                k -= 1
            stack.append(d)
        while k:
            stack.pop()
            k -= 1
        return ''.join(stack).lstrip('0') or '0'


s = Solution()
assert s.removeKdigits('112', 1) == '11'
assert s.removeKdigits('10200', 1) == '200'
assert s.removeKdigits('1432219', 3) == '1219'
assert s.removeKdigits('7865', 2) == '65'
