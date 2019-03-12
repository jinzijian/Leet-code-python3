class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if root == None:
            return 0
        if (p.val<=root.val and q.val>=root.val) or (p.val>=root.val and q.val<=root.val):
            return root
        if p.val<root.val and q.val< root.val:
            return self.lowestCommonAncestor(root.left,p,q)        
        if p.val>root.val and q.val>root.val:
            return self.lowestCommonAncestor(root.right,p,q)        
