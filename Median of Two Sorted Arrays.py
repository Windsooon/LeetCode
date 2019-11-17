class Solution(object):
    # 1. find the kth element 
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

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        if not nums1 and not nums2:
            return
        length = len(nums1) + len(nums2)
        if length % 2 == 0:
            return (self.find(length // 2, nums1, nums2) + self.find(length // 2 - 1, nums1, nums2)) / 2
        else:
            return self.find(length // 2, nums1, nums2)

    def find(self, k, nums1, nums2):
        index_1 = 0
        index_2 = 0
        # k = 1
        while k:
            if index_1 < len(nums1) and index_2 < len(nums2):
                if nums1[index_1] <= nums2[index_2]:
                    index_1 += 1
                else:
                    index_2 += 1
                k -= 1
            elif index_1 < len(nums1):
                return nums1[index_1+k]
            else:
                return nums2[index_2+k]

        if index_1 < len(nums1) and index_2 < len(nums2):
            if nums1[index_1] < nums2[index_2]:
                return nums1[index_1]
            else:
                return nums2[index_2]

        if index_1 < len(nums1):
            return nums1[index_1+k]
        else:
            return nums2[index_2+k]

s = Solution()
nums1 = []
nums2 = [2, 3]
assert (s.findMedianSortedArrays(nums1, nums2)) == 2.5
nums1 = [1, 2]
nums2 = [3, 4]
assert (s.findMedianSortedArrays(nums1, nums2)) == 2.5
nums1 = [1, 3]
nums2 = [2]
assert (s.findMedianSortedArrays(nums1, nums2)) == 2
nums1 = [1, 2]
nums2 = [3]
assert (s.findMedianSortedArrays(nums1, nums2)) == 2
