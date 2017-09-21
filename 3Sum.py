class Solution2(object):
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


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        nums.sort()
        s = set()
        for k, v in enumerate(nums):
            l, r = k+1, len(nums)-1
            while l < r:
                sums = v + nums[l] + nums[r]
                if sums == 0:
                    s.add((v, nums[l], nums[r]))
                    if nums[l] == nums[r]:
                        break
                    l += 1
                    r -= 1
                elif sums > 0:
                    r -= 1
                elif sums < 0:
                    l += 1
        return list(s)

a = Solution()
b = [0, 0, 0, 0]

print(a.threeSum(b))
