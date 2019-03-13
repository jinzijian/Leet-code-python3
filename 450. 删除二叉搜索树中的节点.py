class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root: return None
        if root.val == key:
            if not root.right:
                left = root.left
                return left#为啥看可以直接return left？？

            else:
                right = root.right
                while right.left:#这个循环是为了取到右子树的最小值
                    right = right.left
                root.val, right.val = right.val, root.val
        #这个递归为什么啊
        root.left = self.deleteNode(root.left, key)
        root.right = self.deleteNode(root.right, key)
        return root
