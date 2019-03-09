# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if not head:
            return None
        first=second=head
        while second.next:
            second=second.next
            first=first.next
            if not second.next:
                return first
            else:
                second=second.next
        return first