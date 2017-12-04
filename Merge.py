import time


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def merge_list(first, second):
    '''
    :type first: ListNode
    :type second: ListNode
    merge two non empty singel link list
    '''
    merged_list = first
    while first.next and second:
        tmp = first.next
        first.next = second
        first.next.next = tmp
        second = second.next
        first = tmp
    return merged_list

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
a.next = b
b.next = c
c.next = d


A = ListNode(5)
B = ListNode(6)
C = ListNode(7)
D = ListNode(8)
A.next = B
B.next = C
C.next = D

z = merge_list(a, A)
