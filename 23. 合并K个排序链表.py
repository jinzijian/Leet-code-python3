class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
#思路一遍历一遍所有节点的值，放到数组里然后排序然后赋值给新的链表
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        nodelist = []
        for i in range(len(lists)):
            currentnode = lists[i]
            while currentnode:
                nodelist.append(currentnode)
                currentnode = currentnode.next#不可以直接把值放进去
        nodelist = sorted(nodelist,key = lambda x:x.val)
        
        dummy = ListNode(0)
        cur = dummy
        for i in range(len(nodelist)):
            cur.next = nodelist[i]#不然这里无法赋值
            cur  = cur.next
        return dummy.next  
        #链表的操作都快忘了
