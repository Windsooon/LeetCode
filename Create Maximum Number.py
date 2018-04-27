import heapq


class Solution:
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        def grestest_k_heap(n, k):
            heapq.heapify(n)
            tem = []
            for i in range(k):
                if len(n) >= i+1:
                    tem.append(heapq.nlargest(i+1, n))
            return tem
        tem1 = grestest_k_heap(nums1, k)
        tem2 = grestest_k_heap(nums2, k)
        print(tem1)
        print(tem2)


s = Solution()
num1 = [3, 4, 6, 5]
num2 = [9, 1, 2, 5, 8, 3]
k = 5
s.maxNumber(num1, num2, 5)
