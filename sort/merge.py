class Solution:
    def merge_sort(self, lst):
        if len(lst) == 1:
            return lst
        middle = len(lst) // 2
        left = self.merge_sort(lst[:middle])
        right = self.merge_sort(lst[middle:])
        return self.merge(left, right)

    def merge(self, left, right):
        if not left:
            return right
        elif not right:
            return left
        l_index = r_index = 0
        current = []
        while l_index < len(left) and r_index < len(right):
            if left[l_index] < right[r_index]:
                current.append(left[l_index])
                l_index += 1
            else:
                current.append(right[r_index])
                r_index += 1
        if l_index == len(left):
            current.extend(right[r_index:])
        else:
            current.extend(left[l_index:])
        return current

s = Solusion()
lst = [38, 27, 43, 3, 9, 82, 10]
random.shuffle(lst)
assert(s.select_sort(lst) == [3, 9, 10, 27, 38, 43, 82])
random.shuffle(lst)
assert(s.select_sort(lst) == [3, 9, 10, 27, 38, 43, 82])
s = Solution()
lst = [38, 27, 43, 3, 9, 82, 10]
print(s.merge_sort(lst))
