#自顶部向下，相当于做了n次dfs所以o（n2）
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root == None:
            return True
        if root.left is None and root.right is None:
            return True
        lb = self.isBalanced(root.left)
        rb = self.isBalanced(root.right)
        ld = self.maxdepth(root.left)
        rd = self.maxdepth(root.right)
        if lb and rb and abs(ld-rd)<=1:
            return True
        else:
            return False
    def maxdepth(self,root):
        if root == None:
            return 0
        left = self.maxdepth(root.left)
        right = self.maxdepth(root.right)
        return max(left,right)+1




class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True

        left_depth = self.getDepth(root.left)
        right_depth = self.getDepth(root.right)
        if abs(left_depth - right_depth) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False

    def getDepth(self, root):
        if root == None:
            return 0
        return 1 + max(self.getDepth(root.left), self.getDepth(root.right))
