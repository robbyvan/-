# 404_Sum of Left Leaves
# 按照定义. 
# 如果not, 返回0
# 如果左边是叶, 返回左叶子 + 右子树解
# 否则返回左子树解 + 右子树解

class Solution:
  def sumOfLeftLeaves(self, root):
    if not root:
      return 0
    if root.left and not root.left.left and not root.left.right:
      return root.left.val + self.sumOfLeftLeaves(root.right)
    return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)