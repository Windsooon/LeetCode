import random

class Solusion:
    def insert_sort(self, lst):
        for i in range(1, len(lst)):
            key = lst[i]
            j = i-1
            while j >= 0 and key < lst[j]:
                lst[j+1] = lst[j]
                j -= 1
            lst[j+1] = key
        return lst

s = Solusion()
lst = [38, 27, 43, 3, 9, 82, 10]
random.shuffle(lst)
assert(s.insert_sort(lst) == [3, 9, 10, 27, 38, 43, 82])
random.shuffle(lst)
assert(s.insert_sort(lst) == [3, 9, 10, 27, 38, 43, 82])
