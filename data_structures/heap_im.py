class Solution:
    def __init(self):
        self.lst = []
        self.length = 0

    def insert(self, val):
        self.lst.append(val)
        self.length += 1
        self.move_up(self.length-1)

    def move_up(self, start, index):
        while index > start:
            pass

    def move_down(self, index):
        while self.length > index*2+1:
            left_child = index*2+1
            right_child = index*2+2
            if self.length > right_child:
                if self.lst[right_child] > self.lst[left_child]:
                    min_child = left_child
                else:
                    min_child = right_child
            else:
                min_child = left_child
            self.lst[index], self.lst[min_child] = self.lst[min_child], self.lst[index]
            index = min_child


    def build(self, lst):
        target = len(lst) // 2
        while target > 0:
            self.move_down(target)

    def pop_first(self):
        top = self.lst[0]
        self.lst[0] = self.lst[-1]
        self.lst = self.lst[:-1]
        self.move_down(0)
