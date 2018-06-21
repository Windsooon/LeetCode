class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # binary search
        if num == 1:
            return True
        # 0 5
        left, right = 0, num//2+1
        while right - left > 1:
            # 2
            mid = (left+right)//2
            if mid**2 == num:
                return True
            elif mid**2 > num:
                right = mid
            else:
                # 3
                left = mid
        return False

    def isPerfectSquare2(self, num):
        r = num
        while r*r > num:
            r = (r + num//r) // 2
        return r*r == num


s = Solution()
assert s.isPerfectSquare(16) is True
assert s.isPerfectSquare(9) is True
assert s.isPerfectSquare(14) is False
assert s.isPerfectSquare(5) is False

# assert s.isPerfectSquare2(16) is True
# assert s.isPerfectSquare2(9) is True
# assert s.isPerfectSquare2(14) is False
# assert s.isPerfectSquare2(5) is False
