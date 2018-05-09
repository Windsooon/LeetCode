class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 1:
            return x
        left, right = 1, x
        while 1:
            mid = (left+right)/2
            if mid*mid < x:
                if (int(mid)+1)*(int(mid)+1) > x:
                    return int(mid)
                elif (int(mid)+1)*(int(mid)+1) == x:
                    return int(mid)+1
                else:
                    left = mid
            else:
                right = mid


class Solution2:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # The formula is r**2 - x = 0
        r = x
        while r*r > x:
            r = (r + x/r) / 2
        return r

# x = 0, 1, 2, 3, 4, 8, 9
s = Solution2()
print(s.mySqrt(27))
print(s.mySqrt(7))
