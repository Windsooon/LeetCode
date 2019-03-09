class Solution:
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # awesome solution
        # 3, 1, 4, 2
        prevMax, recordMax = float('-inf'), []
        for e in nums[::-1]:
            # [4]
            if e < prevMax: return True
            while recordMax and recordMax[-1] < e:
                # prevMax = 2
                prevMax = recordMax.pop()
            # [4]
            recordMax.append(e)
        return False

s = Solution()
assert s.find132pattern([1, 2, 3, 4]) is False
assert s.find132pattern([3, 1, 4, 2]) is True
assert s.find132pattern([-1, 3, 2, 0]) is True
assert s.find132pattern([1, 0, 1, -4, -3]) is False
assert s.find132pattern([3, 5, 0, 3, 4]) is True
