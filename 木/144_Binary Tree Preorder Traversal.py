# 144_Binary Tree Preorder Traversal
# 前序遍历, 按照定义, 中, 左, 右,依次访问即可
# (访问中, 右/左依次进栈)

class Solution:
  def preorderTraversal(self, root):
    res, stack = [], [root]
    while stack:
      node = stack.pop()
      if node:
        res.append(node.val)
        stack.append(node.right)
        stack.append(node.left)
    return res
