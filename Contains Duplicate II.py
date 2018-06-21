class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) < 2 or k == 0:
            return False
        tem_dict = {}
        for key, value in enumerate(nums):
            if value in tem_dict and key - tem_dict[value] <= k:
                return True
            tem_dict[value] = key
        return False


s = Solution()
assert s.containsNearbyDuplicate([1, 2, 3, 1], 3) is True
assert s.containsNearbyDuplicate([1, 1], 3) is True
assert s.containsNearbyDuplicate([1, 1], 0) is False
assert s.containsNearbyDuplicate([1, 0, 1, 1], 1) is True
assert s.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2) is False
