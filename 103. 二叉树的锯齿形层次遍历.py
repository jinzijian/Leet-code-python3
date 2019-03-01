class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root :
            return []
        queue = [root]
        res = []
        i = 0
        while queue:
            i = i + 1
            next_queue = []
            if i%2 == 1:
                res.append([node.val for node in queue])
            if i%2 == 0:
                temp1 = [node.val for node in queue]
                temp2 = []
                for k in range(len(temp1)):
                    temp2.insert(0,temp1[k])
                res.append(temp2)  
            for node in queue:
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)    
            queue = next_queue
        return res
