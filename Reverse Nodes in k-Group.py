# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        b = head.next
        print(b.val)
        head.next = head.next.next
        print(head.next.val)
        print(b.val)



a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
a.next = b
b.next = c
c.next = d

s = Solution()
z = s.reverseKGroup(a, 2)

while z:
    z = z.next
