class Solution:
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if k == len(num):
            return '0'
        stack = []
        for n in num:
            while k and stack and stack[-1] > n:
                stack.pop()
                k -= 1
            stack.append(n)
        return ''.join(stack[:k]).lstrip('0') or '0'


s = Solution()
print(s.removeKdigits('1234567', 3))
