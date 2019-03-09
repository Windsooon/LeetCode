class Node(object):
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        self.helper(head)
        return head

    def helper(self, node):
        if not node:
            return node
        stack = []
        while node:
            if not node.next and not node.child:
                if stack:
                    next = stack.pop()
                    node.next = next
                    next.prev = node
                    node = node.next
                else:
                    return node
            elif not node.child:
                node = node.next
            else:
                if node.next:
                    stack.append(node.next)
                node.next = node.child
                node.child.prev = node
                node.child = None
                node = node.next
        return node


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)
g = Node(7)
h = Node(8)
i = Node(9)
j = Node(10)
k = Node(11)
l = Node(12)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
c.child = g
g.next = h
h.next = i
i.next = j
h.child = k
k.next = l
b.prev = a
c.prev = b
d.prev = c
e.prev = d
f.prev = e
h.prev = g
i.prev = h
j.prev = i
l.prev = k

s = Solution()
head = s.flatten(a)
while head:
    print(head.val)
    head = head.next
