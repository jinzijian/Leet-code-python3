'''


解题方法
这个题要求用O(nlongn)的时间复杂度和O(1)的空间复杂度。所以可以使用merge排序，但是如果是链表可以修改指针，把两个有序链表进行原地的合并。

Merge排序就是先划分成一前一后等分的两块，然后对两块分别进行排序，然后再合并两个有序序列。

第一步，如何等分地划分，可以使用快慢指针的方式，当快指针到达结尾，那么慢指针到了中间位置，把链表进行截断分成了两个。

第二步，合并有序的序列，对于单链表来说，正好用到了Merge Two Sorted Lists里的把两个链表合并的方法。

事实上，这个答案里面并不是O(1)的空间，因为，第一，添加了新的链表头的个数会随着递归的次数而不断增加，并不是常量个；第二，递归本身就不是常量空间。
'''

class Solution(object):
    def sortList(self, head):
        if not head or not head.next:
            return head
        pre,slow,fast = head,head,head
        while fast!=None and fast.next!=None:
            pre = slow
            fast = fast.next.next
            slow = slow.next
        pre.next = None
        l1 = head
        l2 = slow
        l1 = self.sortList(head)#递归调用
        l2 = self.sortList(slow)
        return self.mergeTwoLists(l1, l2)
    
    def mergeTwoLists(self, l1, l2):
        head = ListNode(0)
        move = head
        if not l1: return l2
        if not l2: return l1
        while l1 and l2:
            if l1.val < l2.val:
                move.next = l1
                l1 = l1.next
            else:
                move.next = l2
                l2 = l2.next
            move = move.next
        move.next = l1 if l1 else l2
        return head.next
