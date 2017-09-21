class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        an = []
        while lists and lists[0]:
            min_head = lists[0].val
            for k, v in enumerate(lists):
                if not v:
                    lists.pop(k)
                if v.val <= min_head:
                    min_head = v.val
                    answer = (v.val, k)
            lists[k] = lists[k].next
            an.append(answer[0])
        return an

a = Solution()

lists1 = [[1]]
lists2 = [[]]
lists3 = []
