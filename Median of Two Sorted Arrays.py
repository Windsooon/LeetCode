class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len_1, len_2 = len(nums1), len(nums2)
        if (len_1 + len_2) == 0:
            return
        target = (len_1 + len_2) // 2
        if (len_1 + len_2) % 2 != 0:
            return self.k_element(nums1, nums2, target)
        else:
            return (self.k_element(nums1, nums2, target-1)
                    + self.k_element(nums1, nums2, target)) / 2

    def k_element(self, nums1, nums2, k):
        if not nums1:
            return nums2[k]
        if not nums2:
            return nums1[k]
        # 1, 0, 1
        nums1_mid, nums2_mid = len(nums1) // 2, len(nums2) // 2
        if k > (nums1_mid + nums2_mid):
            # [1, 3], [2]
            if nums1[nums1_mid] < nums2[nums2_mid]:
                return self.k_element(nums1[nums1_mid+1:], nums2, k-nums1_mid-1)
            else:
                return self.k_element(nums1, nums2[nums2_mid+1:], k-nums2_mid-1)
        else:
            if nums1[nums1_mid] < nums2[nums2_mid]:
                return self.k_element(nums1, nums2[:nums2_mid], k)
            else:
                return self.k_element(nums1[:nums1_mid], nums2, k)


s = Solution()
# print(s.findMedianSortedArrays([2, 3], [4]))
assert s.findMedianSortedArrays([], []) is None
assert s.findMedianSortedArrays([2], [4]) == 3.0
assert s.findMedianSortedArrays([1, 3], [2]) == 2.0
assert s.findMedianSortedArrays([1, 2], [3, 4]) == 2.5
