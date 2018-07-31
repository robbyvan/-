# 104_Maximum Depth of Binary Tree
# 求树高: max(left, right) + 1

class Solution:
  def maxDepth(self, root):
    if not root:
      return 0
    left = self.maxDepth(root.left)
    right = self.maxDepth(root.right)
    return max(left, right) + 1