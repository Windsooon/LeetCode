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
        def helper(pre, k):
            a = pre
            b = current = pre.next
            for i in range(k):
                next = current.next
                current.next = pre
                pre = current
                current = next
                k -= 1
            a.next, b.next = pre, current
            return b

        count = 0
        dummy = pre = ListNode(0)
        size = dummy.next = pre.next = head
        while size:
            count += 1
            size = size.next
        times = count//k
        while times:
            pre = helper(pre, k)
            times -= 1
        return dummy.next


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
z = s.reverseKGroup(a, 3)

while z:
    print(z.val)
    z = z.next
