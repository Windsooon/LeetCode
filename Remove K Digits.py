class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if k >= len(num):
            return 0
        di = {}
        for i in range(len(num)):
            x = num[i-1:i] if bool(num[i-1:i]) else 0
            if int(num[i]) == 0:
                di[i] = 0
            else:
                di[i] = (int(num[i]) - int(x)) * 10 ** \
                    (len(num) - i) + int(x) * 10 ** (len(num) - i + 1)
        return di

a = Solution()
print(a.removeKdigits('1432219', 3))
