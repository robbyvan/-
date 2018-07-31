# 236_Lowest Common Ancestor of a Binary Tree
# 递归. 如果根是p或q, 返回根
# 否则查看左右子树, 相同的返回规则, 所以LCA出现在left and right的情况(左右各一)
# 如果left, right有一个空, 那么p, q同时出现在了一棵子树, 对那个子树递归查找

class Solution:
  def lowestCommonAncestor(self, root, p, q):
    if not root:
      return None
    if root == p or root == q:
      return root
    left = self.lowestCommonAncestor(root.left, p, q)
    right = self.lowestCommonAncestor(root.right, p, q)

    if left and right:
      return root
    if left:
      return left
    if right:
      return right
    return None
    

  # def __init__(self):
  #   self.maxDepth, self.ancestor = 0, None

  # def lowestCommonAncestor(self, root, p, q):
  #   if not root:
  #     return None
  #   self.ancestor = root
  #   self.checkTargets(root, p, q, 0)
  #   return self.ancestor

  # def checkTargets(self, node, p, q, depth):
  #   hasP, hasQ = False, False
  #   if not node:
  #     return [False, False]
  #   if node == p:
  #     hasP = True
  #   if node == q:
  #     hasQ = True
  #   left = self.checkTargets(node.left, p, q, depth + 1)
  #   right = self.checkTargets(node.right, p, q, depth + 1)
  #   nodeRes = [hasP or left[0] or right[0], hasQ or left[1] or right[1]]
  #   if nodeRes[0] and nodeRes[1] and depth > self.maxDepth:
  #     self.ancestor, self.maxDepth = node, depth
  #   return nodeRes


