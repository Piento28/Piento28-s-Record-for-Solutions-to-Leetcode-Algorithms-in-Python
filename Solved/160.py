# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if (not headA) or (not headB):
            return None
        target = headA
        length_A=length_B=0
        while target:
            target=target.next
            length_A+=1
        target = headB
        while target:
            target=target.next
            length_B+=1
        if length_A<length_B:
            tmp=length_A
            length_A=length_B
            length_B=tmp
            
            tmp=headA
            headA=headB
            headB=tmp
        gap = length_A-length_B
        index_A = headA
        for i in range(gap):
            index_A=index_A.next
        index_B = headB
        while index_A and index_B:
            if index_A is index_B:
                return index_A
            index_A=index_A.next
            index_B=index_B.next
        return None