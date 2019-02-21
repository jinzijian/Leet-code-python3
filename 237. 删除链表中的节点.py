#思路：因为取不到上一个节点 所以把当前节点更改为下一个结点的值然后删除下一个节点
class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node == None:#为了指针合法
            return
        if node.next == None:#为了指针合法
            node = None
            return
        temp = node.next.val
        node.val = temp
        delnode = node.next
        node.next = delnode.next
        return
        
        
