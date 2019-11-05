import random

class Solusion:
    def bobble_sort(self, lst):
        for i in range(len(lst)-1, 0, -1):
            for j in range(i):
                if lst[j] > lst[j+1]:
                    lst[j], lst[j+1] = lst[j+1], lst[j]
        return lst

s = Solusion()
lst = [38, 27, 43, 3, 9, 82, 10]
random.shuffle(lst)
assert(s.bobble_sort(lst) == [3, 9, 10, 27, 38, 43, 82])
random.shuffle(lst)
assert(s.bobble_sort(lst) == [3, 9, 10, 27, 38, 43, 82])
