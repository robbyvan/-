# 226_Invert Binary Tree
# 迭代
class Solution:
  def invertTree(self, root):
    stack = [root]
    while stack:
      node = stack.pop()
      if node:
        node.right, node.left = node.left, node.right
        stack.extend([node.right, node.left])
    return root

# 递归即可
class Solution:
  def invertTree(self, root):
    if not root:
      return root
    root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
    return root