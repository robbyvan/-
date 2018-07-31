# 501_Find Mode in Binary Search Tree
# dfs统计, 选出最高

class Solution:
  def findMode(self, root):
    if not root:
        return []
    d = collections.Counter()
    def dfs(node):
      if node:
        d[node.val] += 1
        dfs(node.left)
        dfs(node.right)
    dfs(root)
    maxVal = max(d.values())
    return [k for k, v in d.items() if v == maxVal]