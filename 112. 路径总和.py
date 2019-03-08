class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None:
            return False
        if root.left == None and root.right == None:
            if root.val == sum:
                return True
        sum = sum - root.val
        return self.hasPathSum(root.left,sum) or self.hasPathSum(root.right,sum)
        
