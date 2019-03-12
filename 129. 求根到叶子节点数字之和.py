class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = self.pathlist(root)
        sum = 0
        for i in res:
            temp = len(i)-1
            for j in i:
                sum += j*10**temp
                temp -= 1
        return sum
    def pathlist(self,root):
        res = []
        if root == None:
            return res
        if not root.left and not root.right:
            res.append([root.val])
            return res
        left = self.pathlist(root.left)
        for i in left:
            i.insert(0,root.val)
            res.append(i)
        right = self.pathlist(root.right)
        for i in right:
            i.insert(0,root.val)
            res.append(i)
        return res
