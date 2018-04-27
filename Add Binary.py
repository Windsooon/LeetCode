class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(int(a, 2) + int(b, 2))[2:]


s = Solution()
print(s.addBinary('11', '1'))
print(s.addBinary('1010', '1011'))
