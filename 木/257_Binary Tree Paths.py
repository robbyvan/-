# 257_Binary Tree Paths
# 普通dfs即可: self.dfs(node.left, path + "->", res)

class Solution:
  def binaryTreePaths(self, root):
    res = []
    if root is None:
      return res
    self.dfs(root, "", res)
    return res

  def dfs(self, node, path, res):
    path = path + str(node.val)
    if (node.left is None) and (node.right is None):
      res.append(path)
      return
    if node.left:
      self.dfs(node.left, path + "->", res)
    if node.right:
      self.dfs(node.right, path + "->", res)
