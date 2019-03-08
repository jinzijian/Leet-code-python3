class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        else:
            return self.ismirror(root.left,root.right)
    def ismirror(self,left,right):
        if left == None and right!=None:
            return False
        if left!=None and right == None:
            return False
        if left == None and right == None:
            return True
        if left.val == right.val:
            return self.ismirror(left.left,right.right) and self.ismirror(left.right,right.left) 
        return False
