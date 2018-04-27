class Solution:
    def combine(self, left, right):
        k = []
        while left and right:
            if left[0] > right[0]:
                k.append(right[0])
                right.pop(0)
            else:
                k.append(left[0])
                left.pop(0)
        if left:
            k.extend(left)
        else:
            k.extend(right)
        return k

    def merge_sort(self, lst):
        if len(lst) <= 1:
            return lst
        lst[:len(lst)//2] = self.merge_sort(lst[:len(lst)//2])
        lst[len(lst)//2:] = self.merge_sort(lst[len(lst)//2:])
        return self.combine(lst[:len(lst)//2], lst[len(lst)//2:])


s = Solution()
lst = [38, 27, 43, 3, 9, 82, 10]
print(s.merge_sort(lst))
