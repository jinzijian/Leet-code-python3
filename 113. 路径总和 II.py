class Solution(object):
    def pathSum(self, root, sum):
        result = []
        if root == None:
            return result
        if root.left== None and root.right==None and sum == root.val:
            result.append([root.val])
            return result
        left = self.pathSum(root.left, sum - root.val)
        for i in left:
            i.insert(0, root.val)
            result.append(i)

        right = self.pathSum(root.right, sum - root.val)
        for i in right:
            i.insert(0, root.val)
            result.append(i)

        return result
        回溯法？？？？
