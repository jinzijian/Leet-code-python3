class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        if root.left == None and root.right == None:
            return True
        if root.left and root.right and (root.left.val > root.val or root.right.val< root.val):
            return False
        if root.left == None and root.right.val<=root.val:
            return False
        if root.right == None and root.left.val >= root.val:
            return False
        self.isValidBST(root.left)
        self.isValidBST(root.right)
        return True
    #这个是错的 原因是没有进行跨层比较
