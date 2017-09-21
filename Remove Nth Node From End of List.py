class Solution:
    def removeNthFromEnd(self, head, n):
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

b = ListNode(1)
c = ListNode(2)
d = ListNode(3)
b.next = c
c.next = d

k = Solution()
print(k.removeNthFromEnd(b, 1))
