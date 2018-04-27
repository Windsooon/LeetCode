class Solution:
    def divide(self, dividend, divisor):
        if (dividend > 0) is (divisor > 0):
            nevigative = 0
        else:
            nevigative = 1
        result = 0
        dividend, divisor = abs(dividend), abs(divisor)
        while dividend >= divisor:
            mul = 1
            tem = divisor
            while dividend >= tem:
                dividend -= tem
                result += mul
                mul <<= 1
                tem <<= 1
        if nevigative:
            result = -result
        return min(max(-2147483648, result), 2147483647)


s = Solution()
print(s.divide(-1, 1))


class Solution:
    def divide(self, dividend, divisor):
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1
        if not positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)
