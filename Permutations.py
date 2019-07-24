import collections

class Solution:
    def permute(self, nums):
        # dp[0] = [1]
        # dp[1] = [[1, 2], [2, 1]]
        if not nums:
            return []
        dic = collections.defaultdict(list)
        dic[0] = [[nums[0]]]
        # 2
        # breakpoint()
        for i in range(1, len(nums)):
            for l in dic[i-1]:
                dic[i].append([nums[i]] + l)
            for l in dic[i-1]:
                dic[i].append(l + [nums[i]])
            for lst in dic[i-1]:
                for x in range(1, len(lst)):
                    dic[i].append(lst[:x] + [nums[i]] + lst[x:])
        return dic[len(nums)-1]


s = Solution()
print(s.permute([1,2,3]))
