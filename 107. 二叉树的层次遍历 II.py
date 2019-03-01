class Solution(object):
    def levelOrderBottom(self, root):
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            next_queue = []
            res.insert(0,[node.val for node in queue])
            for node in queue:
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            queue = next_queue
        return res    
