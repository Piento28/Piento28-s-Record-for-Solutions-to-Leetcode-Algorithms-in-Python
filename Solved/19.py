# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        first = head
        kk = head
        pre_kk = ListNode(0)
        pre_kk.next = head
        i=0
        while i<n-1 and first:
            first=first.next
            i+=1
        if i<n-1:
            return None
        while first.next:
            first=first.next
            kk = kk.next
            pre_kk = pre_kk.next
        pre_kk.next = kk.next
        if kk is head:
            return pre_kk.next
        else:
            return head