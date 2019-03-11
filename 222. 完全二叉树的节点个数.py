#比较左右子树高度 若左右相等则左满右完全 若不等则右满左完全
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        ddl = self.maxdepth(root.left)
        ddr = self.maxdepth(root.right)
        if ddl == ddr:
            return 2**ddl+self.countNodes(root.right)
        else :
            return 2**ddr + self.countNodes(root.left)
        
    
        
    def maxdepth(self,root):
        if root == None:
            return 0
        dl = self.maxdepth(root.left)
        dr = self.maxdepth(root.right)
        return max(dl,dr) + 1
        
