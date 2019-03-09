# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        # import pdb; pdb.set_trace()
        if not head:
            return
        small_position = small_head = ListNode(0)
        big_position = big_head = ListNode(0)
        while head:
            if head.val < x:
                small_position.next = head
                small_position = small_position.next
            else:
                big_position.next = head
                big_position = big_position.next
            head = head.next
        small_position.next = big_head.next
        big_position.next = None
        return small_head.next

a = ListNode(1)
b = ListNode(4)
c = ListNode(3)
d = ListNode(2)
e = ListNode(5)
f = ListNode(2)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
x = 3

s = Solution()
head = s.partition(a, x)
while head:
    print(head.val)
    head = head.next
