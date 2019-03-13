#借用中序遍历
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        res = self.midorder(root)
        return res[k-1]
    def midorder(self,root):
        
        if root == None:
            return []
        res = []
        res += self.midorder(root.left)
        res.append(root.val)
        res += self.midorder(root.right)
        return res
        
