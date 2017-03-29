class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        imax = 0
        count = 0
        table = {0: 0}
        for k, v in enumerate(nums, 1):
            if v == 0:
                count -= 1
            else:
                count += 1
            if count in table:
                imax = max(imax, k-table[count])
            else:
                table[count] = k
        return imax
