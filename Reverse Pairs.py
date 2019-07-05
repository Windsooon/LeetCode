class Solution:
    def reversePairs(self, nums):
        if len(nums) < 2:
            return 0
        self.ans = 0
        self.recursion(nums)
        return self.ans

    def recursion(self, nums):
        if len(nums) == 1:
            return nums
        mid = len(nums)//2
        left = self.recursion(nums[:mid])
        right = self.recursion(nums[mid:])
        return self.combine(left, right)

    def combine(self, left, right):
        count = 0
        r = 0
        for i in range(len(left)):
            while r < len(right) and left[i] > 2*right[r]:
                self.ans += len(left)-i
                r += 1
        return self.merge(left, right)

    def merge(self, left, right):
        lst = []
        l_start = r_start = 0
        while l_start < len(left) and r_start < len(right):
            if left[l_start] <= right[r_start]:
                lst.append(left[l_start])
                l_start += 1
            else:
                lst.append(right[r_start])
                r_start += 1
        if l_start == len(left):
            lst += right[r_start:]
        else:
            lst += left[l_start:]
        return lst


s = Solution()
# print(s.reversePairs([1,3,2,3,1]))
assert s.reversePairs([1,3,2,3,1]) == 2
assert s.reversePairs([2,4,3,5,1]) == 3
# print(s.reversePairs([2,4,3,5,1]))
print(s.reversePairs([5,4,3,2,1]))
