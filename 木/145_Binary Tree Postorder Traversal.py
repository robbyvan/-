# 145_Binary Tree Postorder Traversal
# 后序遍历

class Solution:
  def postorderTraversal(self, root):
    res, stack = [], [root]
    while stack:
      node = stack.pop()
      if node:
        res.append(node.val)
        stack.append(node.left)
        stack.append(node.right)
    return res[::-1]

  # def postorderTraversal(self, root):
  #   res = []
  #   self.helper(root, res)
  #   return res

  # def helper(self, node, res):
  #   if node:
  #     self.helper(node.left, res)
  #     self.helper(node.right, res)
  #     res.append(node.val)