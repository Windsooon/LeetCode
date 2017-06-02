class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        nums.sort()
        lst = []
        for key, out_num in enumerate(nums):
            dic = {}
            for k, inside_num in enumerate((nums[:key] + nums[key+1:])):
                if -(out_num + inside_num) in dic.keys():
                    l = [out_num, inside_num, -(out_num + inside_num)]
                    if l not in lst:
                        lst.append(l)
                else:
                    dic[inside_num] = k
        return lst

a = Solution()
b = [-12,12,-5,-4,-12,11,9,-11,13,1,12,-1,8,1,-9,-11,-13,-4,10,-9,-6,-11,1,-15,-3,4,0,-15,3,6,-4,7,3,-2,10,-2,-6,4,2,-7,12,-1,7,6,7,6,2,10,-13,-3,8,-12,2,-5,-12,6,6,-5,6,-5,-14,9,9,-4,-8,4,2,-7,-15,-11,-7,12,-4,8,-5,-12,-1,12,5,1,-5,-1,5,12,9,0,3,0,3,-14,2,-4,2,-4,0,1,7,-13,9,-1,13,-12,-11,-6,11,-1,-10,-5,-3,10,3,7,-6,-15,-4,10,1,14,-12]

print(a.threeSum(b))
