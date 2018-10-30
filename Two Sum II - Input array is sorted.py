class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i in range(len(numbers)):
            if target-numbers[i] in dic:
                return [dic[(target-numbers[i])]+1, i+1]
            else:
                dic[numbers[i]] = i


numbers = [2,7,11,15]
target = 9
s = Solution()
print(s.twoSum(numbers, target))
