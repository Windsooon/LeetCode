# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, head, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        pre, left = None, head
        while left and left.val != node.val:
            pre, left = left, left.next
        pre.next = left.next
        return head

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
a.next = b
b.next = c
c.next = d
d.next = e


s = Solution()
k = s.deleteNode(a, c)
while k:
    print(k.val)
    k = k.next
