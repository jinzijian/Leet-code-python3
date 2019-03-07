# python没有swap函数 所以要注意要么同时赋值 要么借助一个中间变量

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            
            root.left, root.right =self.invertTree(root.right),self.invertTree(root.left)#同时赋值
        return root
        
