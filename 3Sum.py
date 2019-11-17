class Solution2(object):
    # sort() at the begining
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        nums.sort()
        lst = []
        for a, b in enumerate(nums):
            dic = {}
            for c, d in enumerate(nums[a+1:]):
                if -(b+d) in dic.keys():
                    l = b, d, -(b+d)
                    if l not in lst:
                        lst.append(l)
                else:
                    dic[d] = c
        return lst

a = Solution()
b = [0, 0, 0, 0]

print(a.threeSum(b))
