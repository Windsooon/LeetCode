# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def all(self):
        k = self.next
        while k:
            print(k.val)
            k = k.next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        self.dummy = ListNode(10)
        head = self.recursion(head)
        head.next = None
        return self.dummy.next

    def recursion(self, head):
        if not head:
            return self.dummy
        pre = self.recursion(head.next)
        pre.next = head
        return head


l = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l.next = l2
l2.next = l3
l3.next = l4
l4.next = l5

s = Solution()
k = s.reverseList(l)
while k:
    print(k.val)
    k = k.next
