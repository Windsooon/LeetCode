class Solution:
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if k <= 1:
            return True
        if sum(nums) % k:
            return False
        # 6
        target_sum = sum(nums)/k
        sorted_num = sorted(nums, reverse=True)
        sign = [True] * len(nums)

        # 5, 4, 2, 1
        def dfs(k, start):
            if k == 0:
                return True
            # 5
            current = sorted_num[start]
            if current > target_sum:
                return False
            elif current == target_sum:
                return dfs(k-1, start+1)
            for i in range(len(nums)-1, 0-1, -1):
                if current > target_sum:
                    return False
                elif current == target_sum:
                    return dfs(k-1, start+1)
                else:
                    if sign[i]:
                        current += nums[i]
                        sign[i] = False
        dfs(k, 0)


nums = [5, 2, 4, 1]
s = Solution()
k = s.canPartitionKSubsets(nums, 2)
print(k)
