class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        convert_str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        # 28 % 27 -> dic
        # x1 * 26**n + x2 * 26**n-1 ... xk * 26**0
        ans = []
        # 26 -> Z
        # 27 -> AA
        # 28 -> AB
        # 701 -> ZY
        while n > 0:
            reminder = (n-1) % 26
            ans.append(convert_str[reminder])
            n = (n-1) // 26
        return ''.join(ans[::-1])


s = Solution()
print(s.convertToTitle(1))
print(s.convertToTitle(26))
print(s.convertToTitle(27))
print(s.convertToTitle(28))
print(s.convertToTitle(52))
print(s.convertToTitle(701))
