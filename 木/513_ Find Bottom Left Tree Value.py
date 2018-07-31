# 513_ Find Bottom Left Tree Value
# 还是BFS

class Solution:
  def findBottomLeftValue(self, root):
    q, res = [root], 0
    while q:
      res = q[0].val
      q = [leaf for node in q for leaf in (node.left, node.right) if leaf]
    return res