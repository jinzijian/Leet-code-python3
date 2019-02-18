class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        cur = head
        pre = None
        i = 1
        while (i < m):
            pre = cur
            cur = cur.next
            i += 1
        tail, con = cur, pre    #con 和 tail是锚点用来之后链接
        while (i<n+1):
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
            i += 1
        if con:
            con.next = pre
        else:
            head = pre
        tail.next = cur
        return head
