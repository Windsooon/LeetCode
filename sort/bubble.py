class Solusion:
    def bobble_sort(self, lst):
        for k in range(len(lst)-1, 0, -1):
            for l in range(k):
                if lst[l] > lst[l+1]:
                    lst[l], lst[l+1] = lst[l+1], lst[l]
        return lst


s = Solusion()
lst = [38, 27, 43, 3, 9, 82, 10]
print(s.bobble_sort(lst))
