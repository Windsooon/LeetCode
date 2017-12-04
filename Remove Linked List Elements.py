# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return
        pre = dummy = ListNode(0)
        dummy.next = pre.next = current = head
        while current:
            if current.val == val:
                while current and current.val == val:
                    current = current.next
                pre.next = current
                pre = pre.next
            else:
                pre = current
                current = current.next
        return dummy.next

a = ListNode(1)
b = ListNode(2)
c = ListNode(6)
d = ListNode(4)
e = ListNode(5)
f = ListNode(6)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

g = ListNode(1)
h = ListNode(1)
g.next = h

s = Solution()
z = s.removeElements(g, 1)

while z:
    print(z.val)
    z = z.next
