from collections import deque


class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = deque()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.d.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.d.pop()


    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if self.empty():
            return
        tem = self.d.pop()
        print(tem)
        self.d.append(tem)
        return tem

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return not bool(self.d)


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push('1')
obj.push('2')
param_3 = obj.top()
print(param_3)
