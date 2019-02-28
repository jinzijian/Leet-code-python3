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
    
    
    
    
  #方法二 递归写法
#思路：对于一个节点p，如果p没有左右孩子，我们直接cout p.val，如果p有左右孩子，我们分别加入栈中即可。 前序遍历的reverse
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = list()
        if root == None:
            return result
        
        stack = list()
        stack.append(root)
        while len(stack) != 0:
            top = stack.pop()
            if top.left != None:
                stack.append(top.left)
            if top.right != None:
                stack.append(top.right)

            result.insert(0, top.val)#逆序操作
                
        return result  
