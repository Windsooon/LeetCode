class Solusion:
    def select_sort(self, lst):
        for i in range(len(lst)):
            min_val = (lst[i], i)
            for l in range(i, len(lst)):
                if lst[l] < min_val[0]:
                    min_val = (lst[l], l)
            lst[i], lst[min_val[1]] = lst[min_val[1]], lst[i]
        return lst


s = Solusion()
lst = [38, 27, 43, 3, 9, 82, 10]
print(s.select_sort(lst))
