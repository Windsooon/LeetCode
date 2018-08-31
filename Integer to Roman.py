class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        stack = []

        def helper(number):
            value = [
                (1000, 'M'), (900, 'CM'),
                (500, 'D'), (400, 'CD'),
                (100, 'C'), (90, 'XC'),
                (50, 'L'), (40, 'XL'),
                (10, 'X'), (9, 'IX'),
                (5, 'V'), (4, 'IV'),
                (1, 'I')]
            while number:
                for val in value:
                    if number >= val[0]:
                        stack.append(val[1])
                        return helper(number-val[0])
        helper(num)
        return ''.join(stack)


a = Solution()
print(a.intToRoman(1994))
