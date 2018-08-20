class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sum = l1.val + l2.val
        if sum > 10:
            count = 1
        else:
            count = 0
        sum = sum % 10
        rtype = ListNode(sum)
        while l1.next and l2.next:
            sum = l1.next.val + l2.next.val + count
            if sum > 10:
                count = 1
            else:
                count = 0
            sum = sum % 10
            rtype.next = sum

s = Solution()
s.addTwoNumbers(
