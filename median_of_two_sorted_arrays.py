class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if nums1 is None:
            final_list = nums2
        elif nums2 is None:
            final_list = nums1
        m = len(nums1)
        n = len(nums2)
        a = 0
        b = 0
        now = 0
        final_list = []
        for i in range(round((m+n)/2)-1):
            try:
                nu1 = nums1[a]
            except:
                final_list = nums1.extend(nums2)
            try:
                nu2 = nums2[b]
            except:
                final_list = nums2.extend(nums1)
            print(nu1)
            print(nu2)
            pre = now
            if nu1 <= nu2:
                a += 1
                now = nu2
                print("now %s" % now)
            else:
                b += 1
                now = nu1
        if (m+n) % 2 == 0:
            if final_list:
                return (final_list[(m+n)/2-1]+final_list[(m+n)/2])/2
            else:
                return (pre+now)/2
        else:
            if final_list:
                return final_list[(m+n)/2]
            else:
                return now


nums1 = [1, 2]
nums2 = [3]
solution = Solution()
print(solution.findMedianSortedArrays(nums1, nums2))
