#此题并非自己想出
#关键点 1 创建新节点 2 确保两个长度不同 3跳出循环后还要做一步判断

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        l3 = ListNode(0)
        current = l3
        carry = 0
        while l1 or l2: # 1,1 | None,1 | 1,None
            # Pad 0 if None
            if l1 is None:
                l1v = 0
            else:
                l1v = l1.val
            if l2 is None:
                l2v = 0
            else:
                l2v = l2.val
            # Sum
            tmp = l1v + l2v + carry
            if tmp >= 10:
                x = tmp%10
                carry = int(tmp/10)
            else:
                x = tmp
                carry = 0
            # Assign value
            current.next = ListNode(x)
            current = current.next
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        if carry != 0:
            current.next = ListNode(carry)
        return l3.next
