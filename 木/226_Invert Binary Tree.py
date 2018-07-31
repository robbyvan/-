# 226_Invert Binary Tree
# 递归即可

class Solution:
  def invertTree(self, root):
    stack = [root]
    while stack:
      node = stack.pop()
      if node:
        node.right, node.left = node.left, node.right
        stack.extend([node.right, node.left])
    return root