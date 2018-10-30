class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return nums
        dic = {}
        for n in nums:
            if n in dic.keys():
                dic[n] += 1
            else:
                dic[n] = 1
        # dic = {1: 1, 2: 1}
        lst = [0] * len(nums)
        for key, v in dic.items():
            lst[v-1] = key
        print(lst)
        new_lst = [i for i in lst if i != 0]
        return new_lst[-k:][::-1]


nums = [-1, -1]
k = 1
# nums = [1,1,1,2,2,3]
# k = 2
nums = [1, 2]
k = 2
s = Solution()
print(s.topKFrequent(nums, k))
