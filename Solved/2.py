# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3= lastone = answer = ListNode(0)
        cum = 0
        while l1 and l2:
            tmp = l1.val+l2.val+cum
            l3.val = tmp%10
            cum = tmp//10
            newnode = ListNode(0)
            l3.next = newnode
            lastone = l3
            l3 = l3.next
            l1=l1.next
            l2=l2.next
        while l1:
            tmp = cum+l1.val
            l3.val = tmp%10
            cum = tmp//10
            newnode = ListNode(0)
            l3.next = newnode
            lastone = l3
            l3 = l3.next
            l1=l1.next
        while l2:
            tmp = cum+l2.val
            l3.val = tmp%10
            cum = tmp//10
            newnode = ListNode(0)
            l3.next = newnode
            lastone = l3
            l3 = l3.next
            l2=l2.next
        while cum:
            l3.val = cum%10
            cum = cum//10
            newnode = ListNode(0)
            l3.next = newnode
            lastone =l3
            l3 = l3.next
        if l3.val==0:
            lastone.next = None
        return answer