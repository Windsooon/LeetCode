class Solution(object):
    def say(self, strings):
        pass

    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        return self.say(self.countAndSay(self, n-1))

# 1 -> '1'
# 2 -> '11'
# 3 -> '21'
# 4 -> '1211'
# 5 -> '111221'
# base case 
