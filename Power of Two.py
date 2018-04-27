class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        count = 0
        if n < 0:
            return False
        else:
            element = bin(n)[2:]

        for k in element:
            count += int(k)
        return count == 1


s = Solution()
assert s.isPowerOfTwo(100) is False
assert s.isPowerOfTwo(1) is True
assert s.isPowerOfTwo(2) is True
assert s.isPowerOfTwo(-16) is False
