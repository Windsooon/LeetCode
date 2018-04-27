

class Solution:

    count = 0

    def dp(self, lst, change):
        self.count += 1
        if change in lst:
            return 1
        else:
            return 1 + min(
                [self.dp(lst, change-l) for l in lst if change-l > 0])


s = Solution()
print(s.dp([1, 5, 10, 25], 63))
print(s.count)
