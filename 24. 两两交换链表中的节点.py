class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummyhead = ListNode(0)
        dummyhead.next = head
        p = dummyhead
        while(p.next!=None and p.next.next != None):
            node1 = p.next
            node2 = p.next.next
            node1.next = node2.next
            node2.next = node1
            p.next = node2
            p = node1
        return dummyhead.next
