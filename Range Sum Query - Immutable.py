class NumArray:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return sum(self.nums[i:j+1])

nums = [-2,0,3,-5,2,-1]
obj = NumArray(nums)
param_1 = obj.sumRange(2,5)
print(param_1)
