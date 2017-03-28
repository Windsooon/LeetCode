# first one
class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        k = 11-n
        sum = 9
        while k < 10:
            sum = sum * k
            k = k+1
        return sum + self.countNumbersWithUniqueDigits(n-1)

# better one


class Solution2(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        choices = [9, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        ans, product = 1, 1
        for i in range(n):
            product *= choices[i]
            ans += product
        return ans
