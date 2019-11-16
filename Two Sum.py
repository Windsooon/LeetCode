class Solution:
    # when you need to find two element add up a target
    # can also use in 'presum' trick.
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = dict()
        for i in range(len(nums)):
            if target - nums[i] in dic:
                return [dic[target-nums[i]], i]
            dic[nums[i]] = i
