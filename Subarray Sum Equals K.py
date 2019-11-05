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

class Solution:
    def subarraySum(self, nums, k: int) -> int:
        pre_sum = [0]
        for i in range(len(nums)):
            pre_sum.append(nums[i]+pre_sum[-1])
        seen = dict()
        count = 0
        # sum[i:j] = sum[0:j] - sum[0:i]
        for i in range(len(pre_sum)):
            if pre_sum[i] - k in seen.values():
                count += 1
            seen[i] = pre_sum[i]
        return count

nums = [1, 1, 1]
k = 2
s = Solution()
print(s.subarraySum(nums, k))
