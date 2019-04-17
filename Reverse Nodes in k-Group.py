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
        if not head or not head.next or k == 1:
            return head
        count, current = 0, head
        while count < k:
            count += 1
            if current:
                current = current.next
            else:
                return head
        next = self.reverseKGroup(current, k)
        return self.reverseK(head, k, next)

    def reverseK(self, head, k, next):
        pre = next
        while k:
            k -= 1
            next = head.next
            head.next = pre
            pre = head
            head = next
        return pre


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
a.next = b
b.next = c
c.next = d
d.next = e

f = ListNode(6)

s = Solution()
answer = s.reverseKGroup(a, 6)

while answer:
    print(answer.val)
    answer = answer.next
# 
