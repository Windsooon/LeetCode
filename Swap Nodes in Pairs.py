# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head):
        pre, pre.next = self, head
        # 1, 2, 3, 4
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return self.next

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return
        # [1,2,3,4]
        next = head
        while head and head.next:
            # None
            next_head = self.swapPairs(head.next.next)
            # 2
            next = head.next
            # 
            next.next, head.next = head, next_head
        return next

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
# d = ListNode(4)
a.next = b
b.next = c
# c.next = d

s = Solution()
breakpoint()
k = s.swapPairs(a)


def get_k(k):
    while k:
        print(k.val)
        k = k.next
