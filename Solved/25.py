class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        list_len=0
        tmp=head
        while tmp:
            list_len+=1
            tmp=tmp.next
        if list_len<=1 or k==1 or k>list_len:
            return head
        pre_head=pre_tail=None
        now_head=now_tail=None
        all_head=None
        i=0
        first=None
        second=head
        third=head.next
        while i<(list_len-list_len%k):
            now_head=second
            for j in range(k-1):
                second.next=first
                first=second
                second=third
                third=third.next
            second.next=first
            now_tail=second
            if i==0:
                all_head=now_tail
            else:
                pre_head.next=now_tail
            i+=k-1
            if i+1<(list_len-list_len%k):
                i+=1
                first=None
                second=third
                third=third.next
                pre_head=now_head
                pre_tail=now_tail
            else:
                break
        if third==None:
            return all_head
        else:
            now_head.next=third
            return all_head