class Solution:
    def candy(self, ratings):
        nums = [1] * len(ratings)
        # from left to right
        for i in range(len(ratings)-1):
            if ratings[i+1] > ratings[i]:
                nums[i+1] = nums[i] + 1
        # from right to left
        for i in range(len(ratings)-1, 0, -1):
            if ratings[i] < ratings[i-1] and nums[i-1] <= nums[i]:
                nums[i-1] = nums[i] + 1
        return sum(nums)


s = Solution()
assert s.candy([1, 0, 2]) == 5
assert s.candy([1, 2, 2]) == 4
assert s.candy([1, 2, 3, 4, 5]) == 15
assert s.candy([4, 5, 3]) == 4
assert s.candy([1, 2, 87, 87, 87, 2, 1]) == 13
assert s.candy([29,51,87,87,72,12]) == 12
