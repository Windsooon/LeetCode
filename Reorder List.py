# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        def reverse_list(node):
            '''
            :type node: ListNode
            reverse a non-empty single link list
            '''
            pre = None
            while node:
                next = node.next 
                node.next, pre, node = pre, node, next
            return pre

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

        if not head:
            return head
        fast = slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        middle = slow
        half_reverse = reverse(middle)
        slow.next = None
        merge_list(
