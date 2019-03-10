class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        sum = self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)#递归
        if root.left and root.left.left is None and root.left.right is None:#判断是否是左叶子节点
            sum += root.left.val
        return sum
