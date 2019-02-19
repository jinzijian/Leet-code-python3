class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummyhead = ListNode(0)#虚拟头节点法
        dummyhead.next = head
        cur = dummyhead
        while cur.next!= None:
            if(cur.next.val == val):
                delnode = cur.next
                cur.next = delnode.next
            else:
                cur = cur.next
        return dummyhead.next    
