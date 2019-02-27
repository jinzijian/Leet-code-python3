#方法一 递归算法实现
class Solution:
    def __init__(self):
        self.ret = []#必须要在这里声明一个属性不然每次调用就被置零了
        
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root != None:
            self.ret.append(root.val)
            self.preorderTraversal(root.left)
            self.preorderTraversal(root.right)
            
        return self.ret
    
#方法二 迭代算法实现---用栈
class Solution:
    
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if root == None:
            return result

        stack = []
        stack.append(root)
        while(len(stack))!=0:
            top = stack.pop()
            if top.right!=None:
                stack.append(top.right)
            if top.left!=None:
                stack.append(top.left)    
            result.append(top.val)    
        return result    
            
