class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None :#注意给的是不是空链表
            return head
        dummyhead = ListNode(0)
        dummyhead.next = head
        slow = dummyhead
        fast = slow.next
        i = 0
        count = head
        while count!= None:
            i+= 1
            count = count.next   
        if i == 1:
            return head
        j = 0
        k = k%i
        if k == 0:#注意k的取值
            return head
        while j<k:
            j += 1
            fast = fast.next
        while fast.next!=None:
            slow = slow.next
            fast = fast.next
        slow = slow.next    
        new = slow.next
        slow.next = None
        fast.next = dummyhead.next
        return new
