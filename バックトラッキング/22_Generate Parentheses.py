# 22_Generate Parentheses
# 普通dfs, 限制: 还有left, right可用 & left不多于right

class Solution:
  def generateParenthesis(self, n):
    if n < 0:
      return []
    res = []
    self.helper(n, n, "", res)
    return res

  def helper(self, left, right, path, res):
    if right < left:
      return
    if left == 0 and right == 0:
      res.append(path)
      return
    if left > 0:
      self.helper(left - 1, right, path + "(", res)
    if right > 0:
      self.helper(left, right - 1, path + ")", res)
