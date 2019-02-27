#方法一 递归算法实现
class Solution:
    def __init__(self):
        self.ret = []#必须要在这里声明一个属性不然每次调用就被置零了
        
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root != None:
            self.ret.append(root.val)
            self.preorderTraversal(root.left)
            self.preorderTraversal(root.right)
            
        return self.ret
