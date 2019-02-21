
class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head==None or head.next==None:
            return head
            
        dummy=ListNode(0)
        dummy.next=head
        pre=dummy
        cur=dummy.next
        
        while cur!=None:
            while cur.next and cur.next.val==pre.next.val:
                cur=cur.next
            if pre.next==cur:
                pre=pre.next
            else:
                pre.next=cur.next
            cur=cur.next
        return dummy.next
