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
                return False, first
            second=second.next
            if first is second:
                return True, first
        return False, first
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        flag, second = self.hasCycle(head)
        if flag:
            first=head
            while not(first is second):
                first=first.next
                second=second.next
            return first
        else:
            return None

