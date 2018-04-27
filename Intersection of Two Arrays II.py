class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        ans = []
        for k in nums1:
            if k in nums2:
                del nums2[nums2.index(k)]
                ans.append(k)
        return ans

s = Solution()
print(s.intersect([1, 2, 2, 1], [2, 2]))
