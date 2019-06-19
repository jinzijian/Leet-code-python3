class Solution(object):
    #中序遍历之后判断数组是否严格递增
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)

        res = []
        if not root:
            return True
        inorder(root)
        for i in range(1, len(res)):
            if res[i]<= res[i-1]:
                return False
        return True
        
        
