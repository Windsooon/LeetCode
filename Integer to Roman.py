class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        d = {
            0: ['', 'M', 'MM', 'MMM'],
            1: ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
            2: ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
            3: ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'],
        }
        return d[0][num//1000] + d[1][num % 1000//100] + \
            d[2][num % 100//10] + d[3][num % 10]

a = Solution()
print(a.intToRoman(3999))
