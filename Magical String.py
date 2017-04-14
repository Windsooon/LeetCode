class Solution(object):
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        base_str = "122"
        k = 2

        while len(base_str) < n:
            curr = base_str[k]
            u = "2" if base_str[-1] == "1" else "1"
            base_str += u*int(curr)
            k += 1
        return base_str[:n].count('1')


b = Solution()
print(b.magicalString(10))
