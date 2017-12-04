# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return
        count = 0
        length = head
        while length:
            count += 1
            length = length.next
        rotate = k % count
        if k == 0 or rotate == 0:
            return head
        fast = slow = head

        while rotate:
            fast = fast.next
            rotate -= 1
        while fast.next:
            fast = fast.next
            slow = slow.next
        tmp = slow.next
        fast.next = head
        slow.next = None
        return tmp


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
a.next = b
b.next = c
c.next = d
d.next = e

x = y = ListNode(1)
y.val = 10

s = Solution()
z = s.rotateRight(a, 2)
