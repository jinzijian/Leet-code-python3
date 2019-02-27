#方法一：递归方法
#左子树 ---> 根结点 ---> 右子树

class Solution(object):
    def __init__(self):
        self.ret = []#必须要在这里声明一个属性不然每次调用就被置零了
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root != None:
            self.inorderTraversal(root.left)
            self.ret.append(root.val)
            self.inorderTraversal(root.right)
        return self.ret
        
        
