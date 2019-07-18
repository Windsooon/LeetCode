class Solution:
    def matrixReshape(self, nums, r: int, c: int):
        # can't reshape
        if r * c > len(nums) * len(nums[0]):
            return nums
        lst = []
        for i in range(len(nums)):
            for j in range(len(nums[0])):
                lst.append(nums[i][j])
        new_nums = [[0] * c for i in range(r)]
        position = 0
        for i in range(len(new_nums)):
            for j in range(len(new_nums[0])):
                new_nums[i][j] = lst[position]
                position += 1
        return new_nums

s = Solution()
s.matrixReshape('df', 10,10)

