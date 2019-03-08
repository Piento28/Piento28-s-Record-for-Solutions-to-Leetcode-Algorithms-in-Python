# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        for i in range(len(lists)-1,-1,-1):
            if lists[i]==None:
                del lists[i]
        if len(lists)==0:
            return None
        last=second=start = ListNode(0)
        while lists:
            count_min = 2147483648
            count_index = 0
            for i in range(len(lists)):
                if lists[i].val<count_min:
                    count_min = lists[i].val
                    count_index = i
            last.val = lists[count_index].val
            newnode = ListNode(0)
            last.next = newnode
            second = last
            last = last.next
            
            lists[count_index]=lists[count_index].next
            if not lists[count_index]:
                del lists[count_index]
        if last.val==0:
            second.next = None
        return start

# # Solution, standard iterative binary divide and conquer:
# class Solution(object):
#     def mergeKLists(self, lists):
#         """
#         :type lists: List[ListNode]
#         :rtype: ListNode
#         """
#         amount = len(lists)
#         interval = 1
#         while interval < amount:
#             for i in range(0, amount - interval, interval * 2):
#                 lists[i] = self.merge2Lists(lists[i], lists[i + interval])
#             interval *= 2
#         return lists[0] if amount > 0 else lists

#     def merge2Lists(self, l1, l2):
#         head = point = ListNode(0)
#         while l1 and l2:
#             if l1.val <= l2.val:
#                 point.next = l1
#                 l1 = l1.next
#             else:
#                 point.next = l2
#                 l2 = l1
#                 l1 = point.next.next
#             point = point.next
#         if not l1:
#             point.next=l2
#         else:
#             point.next=l1
#         return head.next