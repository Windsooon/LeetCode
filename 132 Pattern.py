class Solution:
    def find132pattern(self, nums):
        if len(nums) < 3:
            return False
        current_min = [nums[0]]
        for i in range(len(nums)):
            current_min.append(min(nums[i], current_min[-1]))
        stack = []
        for i in range(len(nums)):
            while stack and stack[-1] > nums[i]:
                top = stack.pop()
                if nums[i] > current_min[i]:
                    return True
            stack.append(nums[i])
        return False

s = Solution()
assert s.find132pattern([1, 2, 3, 4]) is False
assert s.find132pattern([3, 1, 4, 2]) is True
assert s.find132pattern([-1, 3, 2, 0]) is True
assert s.find132pattern([1, 0, 1, -4, -3]) is False
assert s.find132pattern([3, 5, 0, 3, 4]) is True
