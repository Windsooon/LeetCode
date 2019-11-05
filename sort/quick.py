import random

class Solution:
    def quick_sort(self, lst):
        if not lst:
            return []
        if len(lst) == 1:
            return lst
        target = 0
        index = len(lst)-1
        for i in range(1, len(lst)):
            if i <= index:
                while lst[i] > lst[target] and i <= index:
                    lst[i], lst[index] = lst[index], lst[i]
                    index -= 1
            else:
                break
        lst[target], lst[index] = lst[index], lst[target]
        left = self.quick_sort(lst[:index])
        right = self.quick_sort(lst[index+1:])
        return left + [lst[index]] + right

s = Solution()
lst = [38, 27, 43, 3, 9, 82, 10]
assert(s.quick_sort(lst) == [3, 9, 10, 27, 38, 43, 82])
