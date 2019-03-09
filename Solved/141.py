# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        first = second = head
        while second and first:
            second=second.next
            first=first.next
            if not second:
                return False
            second=second.next
            if first is second:
                return True
        return False