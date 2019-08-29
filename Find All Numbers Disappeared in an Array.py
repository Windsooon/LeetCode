class Solution:
    def findDisappearedNumbers(self, nums):
        ans = []
        for i in range(len(nums)):
            index = abs(nums[i])-1
            nums[index] = -(abs(nums[index]))
        for i in range(len(nums)):
            if nums[i] > 0:
                ans.append(i+1)
        return ans

s = Solution()
lst = [4,3,2,7,8,2,3,1]
print(s.findDisappearedNumbers(lst))
