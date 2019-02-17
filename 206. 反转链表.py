class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = None
        while(head!=None):
            temp = head.next
            head.next = pre
            pre = head
            head = temp
        return pre
