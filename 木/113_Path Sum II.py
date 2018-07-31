# 113_Path Sum II
# 递归套路 helper(node, target, path, res)
# 成功条件 => if not root.left and not root.right and root.val == target

class Solution:
  def pathSum(self, root, target):
    res = []
    self.dfs(root, target, [], res)
    return res

  def dfs(self, root, target, path, res):
    if not root:
      return
    if not root.left and not root.right and root.val == target:
      path.append(root.val)
      res.append(path)
      return
    self.dfs(root.left, target - root.val, path + [root.val], res)
    self.dfs(root.right, target - root.val, path + [root.val], res)