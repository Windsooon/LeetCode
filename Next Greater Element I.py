class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if not nums1 or not nums2:
            return []
        dic = {}
        stack = []
        for i in range(len(nums2)):
            while stack and stack[-1] < nums2[i]:
                tem = stack.pop()
                dic[tem] = nums2[i]
            stack.append(nums2[i])
        
        ans = []
        for i in range(len(nums1)):
            if nums1[i] in dic:
                ans.append(dic[nums1[i]])
            else:
                ans.append(-1)
        return ans

nums1 = [2,4]
nums2 = [1,2,3,4]

s = Solution()
print(s.nextGreaterElement(nums1, nums2))
