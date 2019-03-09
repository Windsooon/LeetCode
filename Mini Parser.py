class Solution(object):
    def deserialize(self, s):
        pass

# 44
# []
# [[]]
# [[33]]
# [33]
# [44, []]
# [44, [34, 54], 45]


ele = '[123,234,[456,[789]],999]'
s = Solution()
print(s.deserialize(ele))
