class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lst = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.lst:
            self.min_val = x
        self.lst.append(x-self.min_val)
        if x-self.min_val < 0:
            self.min_val = x
        

    def pop(self):
        """
        :rtype: void
        """
        k = self.lst.pop()
        if k < 0:
            self.min_val = self.min_val - k
        

    def top(self):
        """
        :rtype: int
        """
        if self.lst[-1] <= 0:
            return self.min_val
        else:
            return self.lst[-1] + self.min_val

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_val

    def get_lst(self):
        return self.lst


obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.get_lst())
obj.pop()
print(obj.top())
print(obj.getMin())
