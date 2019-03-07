#注意结束的条件 以及递归的return函数最好包含递归本身
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:
            return True
        if p is None or q is None or p.val!=q.val:
            return False
        return self.isSameTree(p.left,q.left)and self.isSameTree(p.right,q.right)
