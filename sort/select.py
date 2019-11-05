import random

class Solusion:
    def select_sort(self, lst):
        for i in range(len(lst)):
            min_index = i
            for j in range(i+1, len(lst)):
                if lst[j] < lst[min_index]:
                    min_index = j
            lst[i], lst[min_index] = lst[min_index], lst[i]
        return lst


s = Solusion()
lst = [38, 27, 43, 3, 9, 82, 10]
random.shuffle(lst)
assert(s.select_sort(lst) == [3, 9, 10, 27, 38, 43, 82])
random.shuffle(lst)
assert(s.select_sort(lst) == [3, 9, 10, 27, 38, 43, 82])
