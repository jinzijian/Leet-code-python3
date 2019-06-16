#迭代做法
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = None
        while head is not None:
            temp = head.next
            head.next = pre
            pre = head
            head = temp
        return pre
    
#递归解决
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        newhead = self.reverseList(head.next)#此时head.next为反转后链表的尾节点
        head.next.next = head #把head接到head.next后面
        head.next = None
        return newhead
