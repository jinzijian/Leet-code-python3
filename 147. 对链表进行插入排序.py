#领悟的真的很艰难
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head is None or head.next is None:
            return head
        
        dummy=ListNode(0)
        dummy.next=head
        cur=head
        while cur.next:
            if cur.val > cur.next.val:#判断是否要进行插入操作
                pre = dummy
                while pre.next.val < cur.next.val:#循环用来让pre指到需要做交换操作的节点
                    pre = pre.next
                temp = cur.next
                cur.next = temp.next
                temp.next = pre.next
                pre.next = temp
            else:
                cur = cur.next
        return dummy.next      
