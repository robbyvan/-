# 102_Binary Tree Level Order Traversal
# 利用queue, 每层扫描进队列即可
class Solution:
  def levelOrder(self, root):
    if not root:
      return []
    stack, res, odd = [root], [], True
    while stack:
      nextStack = []
      path = []
      for node in stack:
        path.append(node.val)
        if not (node.left is None):
          nextStack.append(node.left)
        if not (node.right is None):
          nextStack.append(node.right)
      stack = nextStack
      res.append(path)
    return res
