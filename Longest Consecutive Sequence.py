class Solution(object):
    def longestConsecutive(self, nums):
        max_length = 0
        length = 1
        dic = {}
        set_nums = set(nums)
        for num in set_nums:
            if num not in dic:
                if num-1 not in set_nums:
                    val = num+1
                    while val in set_nums:
                        dic[val] = 1
                        length += 1
                        val += 1
                    max_length = max(max_length, length)
                    length = 1
        return max_length


s = Solution()
len = s.longestConsecutive([100, 1, 3, 2, 4, 200])
# len = s.longestConsecutive([0])
print(len)
