# 103_Binary Tree Zigzag Level Order Traversal
# 还是BFS按层扫描

class Solution:
  def zigzagLevelOrder(self, root):
    res = []
    if not root:
      return res
    q, foward = [root], True

    while q:
      nextLevel, nodes = [], []
      for node in q:
        nodes.append(node.val)
        if node.left:
          nextLevel.append(node.left)
        if node.right:
          nextLevel.append(node.right)
      if foward:
        res.append(nodes)
      else:
        res.append(nodes[::-1])
      q = nextLevel
      foward = not foward
    return res