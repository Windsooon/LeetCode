class Solution:
    # maintain a pointer current to indicate which one to exchange
    def removeDuplicates(self, nums: List[int]) -> int:
        current = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[current] = nums[i]
                current += 1
        return current

s = Solution()
lst = [1, 1, 2]
assert s.removeDuplicates(lst), 2
