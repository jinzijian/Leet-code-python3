class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = None
        cur = head
        while (cur!= None and cur.next!= None):
            if cur.val == cur.next.val:#val才能读出值
                cur.next = cur.next.next    
            else:#别忘了else
                cur = cur.next
        return head  
