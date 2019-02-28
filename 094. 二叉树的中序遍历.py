#方法一：递归方法
#左子树 ---> 根结点 ---> 右子树

class Solution(object):
    def __init__(self):
        self.ret = []#必须要在这里声明一个属性不然每次调用就被置零了
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root != None:
            self.inorderTraversal(root.left)
            self.ret.append(root.val)
            self.inorderTraversal(root.right)
        return self.ret
# 方法二：迭代算法
#我们先把节点所有的左节点放入栈中，然后开始出栈，每次出栈都把栈中的元素放入到结果中，并且把
#每个结果的右孩子放入栈中。因此，这里的遍历顺序就是左->中->右。
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        res = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            root = stack.pop()
            res.append(root.val)
            root = root.right        
        
