class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if not isinstance(n, int) or n < 1:
            return False
        seen_num = {}
        str_n = str(n)
        seen_num[str_n] = 1
        while 1:
            sum_val = sum(int(s)**2 for s in str_n)
            if sum_val == 1:
                return True
            elif str(sum_val) in seen_num:
                return False
            seen_num[str(sum_val)] = 1
            str_n = str(sum_val)


s = Solution()
assert s.isHappy(19) is True
assert s.isHappy(2) is False
assert s.isHappy(0) is False
assert s.isHappy(1) is True
assert s.isHappy(82) is True
assert s.isHappy(4.4) is False
assert s.isHappy(-4.4) is False
