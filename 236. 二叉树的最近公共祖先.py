class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        解题思路
        最低公共祖先的定义是，在一个二叉树中，我们能找到的最靠近叶子的节点，该节点同时是p和q的祖先节点。注意，如果p或者q本身也可以作为自己的祖先。

如果用递归的话，最重要的还是明白递归函数的作用是什么。这个题里面lowestCommonAncestor(root, p, q)函数的作用是判断p和q在root树中最低的公共祖先是什么，返回值是公共祖先。

这个题的模式叫做devide and conquer. 如果当前节点等于其中的p和q某一个节点，那么找到了节点，返回该节点，否则在左右子树分别寻找。

左右子树两个返回的是什么呢？按照该递归函数的定义，即找到了左子树和右子树里p和q的公共祖先，注意祖先可以是节点自己。然后根据左右侧找到的节点做进一步的判断。

如果左右侧查找的结果都不为空，说明分别找到了p和q，那么LCA就是当前节点。否则就在不为空的那个结果就是所求。

        """
        if root == None:
            return None
        if root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left if left else right
