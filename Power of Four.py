class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num != 0 and num & (num-1) == 0 and num % 3 == 1

s = Solution()
assert s.isPowerOfFour(0) is False
assert s.isPowerOfFour(5) is False
assert s.isPowerOfFour(16) is True
assert s.isPowerOfFour(400) is False
