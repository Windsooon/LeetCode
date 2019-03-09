class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists):
        res = current = ListNode(0)
        next = self.get_next(lists)
        while next:
            current.next = next
            current = current.next
            next = self.get_next(lists)
        return res.next

    def get_next(self, lists):
        min_val = float('inf')
        min_index = -1
        for i in range(len(lists)):
            if lists[i] and lists[i].val < min_val:
                min_val = lists[i].val
                min_index = i
        if min_index == -1:
            return
        tem = lists[min_index]
        lists[min_index] = lists[min_index].next
        return tem


a = ListNode(1)
b = ListNode(4)
c = ListNode(5)
a.next = b
b.next = c
d = ListNode(1)
e = ListNode(3)
f = ListNode(4)
d.next = e
e.next = f
g = ListNode(2)
h = ListNode(6)
g.next = h

lists = [a, d, g]
s = Solution()
z = s.mergeKLists(lists)
while z:
    print(z.val)
    z = z.next
