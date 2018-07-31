# 111_Minimum Depth of Binary Tree
# 还是BFS

class Solution:
  def minDepth(self, root):
    if not root:
      return 0
    q, depth = [root], 0
    while q:
      depth += 1
      nextQ = []
      for node in q:
        if node and (node.left is None) and (node.right is None):
          return depth
        if node.left:
          nextQ.append(node.left)
        if node.right:
          nextQ.append(node.right)
      q = nextQ
    return depth
