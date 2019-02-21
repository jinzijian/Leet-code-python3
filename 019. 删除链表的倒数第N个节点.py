# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#思路 快慢指针距离为n 进行滑动
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummyhead = ListNode(0)
        dummyhead.next = head
        slow = dummyhead
        fast = slow.next
        i = 0
        while i<n:
            i += 1
            fast = fast.next
        while fast!=None:
            slow = slow.next
            fast = fast.next
        temp = slow.next
        slow.next = temp.next
        return dummyhead.next
