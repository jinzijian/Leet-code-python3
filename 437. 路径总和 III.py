class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if root == None:
            return 0
        result = self.findpath(root,sum)
        result += self.pathSum(root.left,sum)
        result += self.pathSum(root.right,sum)        
        return result
    def findpath(self,root,sum):
        result = 0
        if root == None:
            return 0
        if root.val == sum:
            result += 1
        result = result + self.findpath(root.left,sum-root.val)
        result = result + self.findpath(root.right,sum-root.val)
        return result#位置很关键
        
