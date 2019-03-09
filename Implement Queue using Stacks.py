class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.int_stack = []
        self.out_stack = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.int_stack.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if not self.out_stack:
            self.move()
        return self.out_stack.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if not self.out_stack:
            self.move()
        return self.out_stack[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not self.int_stack and not self.out_stack

    def move(self):
        while self.int_stack:
            self.out_stack.append(self.int_stack.pop())


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
print(obj.push(1))
print(obj.push(2))
print(obj.peek())
print(obj.push(3))
print(obj.peek())
