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
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        # 1->2->3->4->5
        # prev->None
        prev = head
        current = head.next
        print(current is head.next)
        prev.next = None
        print(current is head.next)
        # current = 2
        while current:
            # next = 3
            next = current.next
            # 2->1->None
            current.next = prev
            prev = current
            current = next
        return prev

    def reverseList2(self, head):
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev


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
