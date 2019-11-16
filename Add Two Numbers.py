# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 1. while l1 or l2 or add_one is the key
    # edge case:
    # l1 = 5
    # l2 = 5
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = start = ListNode(None)
        add_one = 0
        while l1 or l2 or add_one:
            if l1:
                add_one += l1.val
                l1 = l1.next
            if l2:
                add_one += l2.val
                l2 = l2.next
            start.val = add_one % 10
            add_one //= 10
            if l1 or l2 or add_one:
                start.next = ListNode(None)
                start = start.next
        return dummy


a = ListNode(2)
b = ListNode(4)
c = ListNode(3)
a.next = b
b.next = c

d = ListNode(5)
e = ListNode(6)
f = ListNode(4)
d.next = e
e.next = f

s = Solution()
dummy = s.addTwoNumbers(a, d)
while dummy:
    print(dummy.val)
    dummy = dummy.next

