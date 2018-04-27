class Solusion:
    def helper(self, lst, n):
        '''
        Sort first n elements in lst
        '''
        if n <= 1:
            return lst
        lst = self.helper(lst, n-1)
        last = lst[n-1]
        num = n-1
        while num > 0 and lst[num-1] > last:
            lst[num] = lst[num-1]
            num -= 1
        lst[num] = last
        return lst

    def insert_sort_recursive(self, lst):
        return self.helper(lst, len(lst))
