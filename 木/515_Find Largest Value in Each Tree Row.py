# 515_Find Largest Value in Each Tree Row
# 还是BFS...

class Solution:
  def largestValues(self, root):
    if not root:
      return []
    q, res = [root], []
    while q:
      res.append(max(node.val for node in q))
      q = [leaf for node in q for leaf in (node.left, node.right) if leaf]
    return res