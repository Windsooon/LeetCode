class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans = []
        for n in nums1:
            index = nums2.index(n)
            for i in range(index+1, len(nums2)):
                if nums2[i] > n:
                    ans.append(nums2[i])
                    break
            else:
                ans.append(-1)
        return ans

nums1 = [2,4]
nums2 = [1,2,3,4]

s = Solution()
print(s.nextGreaterElement(nums1, nums2))
