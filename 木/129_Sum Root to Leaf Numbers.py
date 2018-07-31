# 129_Sum Root to Leaf Numbers
# 基本dfs + helper, 拼path, 添加到res

class Solution:
  def sumNumbers(self, root):
    path, res = 0, [0]
    self.helper(root, "", res)
    return res[0]

  def helper(self, root, path, res):
    if not root:
      return
    if not root.left and not root.right:
      path += str(root.val)
      res[0] += int(path)
      return
    self.helper(root.left, path + str(root.val), res)
    self.helper(root.right, path + str(root.val), res)