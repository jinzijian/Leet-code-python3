#借用二叉搜索树的性质 中间的为根节点
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        length = len(nums)
        if length == 0:
            return None
        if length == 1:
            return TreeNode(nums[0])
        root = TreeNode(nums[length / 2])
        root.left = self.sortedArrayToBST(nums[:length/2])
        root.right = self.sortedArrayToBST(nums[length/2+1:])
        return root
