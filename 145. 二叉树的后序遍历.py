#方法一：递归算法
class Solution(object):
    def __init__(self):
        self.ret = []#必须要在这里声明一个属性不然每次调用就被置零了
    def postorderTraversal(self, root):
        if root == None:
            return []
        self.postorderTraversal(root.left)        
        self.postorderTraversal(root.right)
        self.ret.append(root.val)
        return self.ret
