#思路：因为取不到上一个节点 所以把当前节点更改为下一个结点的值然后删除下一个节点
class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
        
        
