# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return
        elif not head.next:
            return head
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        tem = slow.next
        slow.next = None
        first = self.sortList(head)
        second = self.sortList(tem)
        return self.merge(first, second)

    def merge(self, first, second):
        dummy = current = ListNode(1)
        while first and second:
            if first.val > second.val:
                current.next = second
                second = second.next
            else:
                current.next = first
                first = first.next
            current = current.next
        if first:
            current.next = first
        else:
            current.next = second
        return dummy.next

a = ListNode(4)
b = ListNode(2)
c = ListNode(1)
d = ListNode(3)
a.next = b
b.next = c
c.next = d

s = Solution()
s.sortList(a)
