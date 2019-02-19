#思路把两个数加起来再赋给一个新的链表
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        nums1 = ""
        nums2 = ""
        while l1!= None:
            nums1+= str(l1.val)
            l1 = l1.next
        while l2!= None:
            nums2+= str(l2.val)
            l2 = l2 .next
        add = str(int(nums1)+int(nums2))
        head = ListNode(add[0])
        answer = head
        for i in range(1,len(add)):
            node = ListNode(add[i])
            head.next = node
            head = head.next
        return answer    
        #方法二用栈完成暂时不会
