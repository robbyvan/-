# 107_Binary Tree Level Order Traversal II
# bfs + list.insert(index, obj)倒序插入即可.

class Solution:
  def levelOrderBottom(self, root):
    if not root:
      return []
    q, res = [root], []
    while q:
      nextlevel, path = [], []
      for node in q:
        if node:
          path.append(node.val)
          if node.left:
            nextlevel.append(node.left)
          if node.right:
            nextlevel.append(node.right)
      res.insert(0, path)
      q = nextlevel
    return res
