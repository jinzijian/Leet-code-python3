class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        depl = self.maxDepth(root.left)
        depr = self.maxDepth(root.right)
        return max(depl,depr)+1
        
