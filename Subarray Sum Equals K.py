from queue import Queue
class Solution:
    def subarraySum(self, nums, k):
        # base case 
        if not nums:
            return 0
        elif len(nums) == 1 and nums[0] == k:
            return 1
        count = 0
        q = Queue()
        for i in range(len(nums)):
            q.put((i, nums[i]))
        while not q.empty():
            index, val = q.get()
            if val == k:
                count += 1
            index += 1
            if index < len(nums):
                val += nums[index]
                q.put((index, val))
        return count

nums = [1, 1, 1]
k = 2
s = Solution()
print(s.subarraySum(nums, k))
