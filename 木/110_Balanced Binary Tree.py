# 110_Balanced Binary Tree
# 递归, 求解左右孩子节点的的孩子高度.然后作差是该节点的结果(-1不满足, 或者孩子高度差0, 1)
# 基本算法: 求树的深度 1 + max(left, right).

class Solution:
  def isBalanced(self, root):
    def height(root):
      if root is None:
        return 0
      left = height(root.left)
      right = height(root.right)
      if left == -1 or right == -1 or abs(left - right) > 1:
        return -1
      return 1 + max(left, right)
    return height(root) != -1