class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        level = 1
        sum = 0
        for d in digits[::-1]:
            sum += level * d
            level = level * 10
        sum += 1
        return [int(x) for x in str(sum)]



s = Solution()
# print(s.plusOne([4,3,2,1]))
print(s.plusOne([0]))
