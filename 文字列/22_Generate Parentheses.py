# 22_Generate Parenthesis
# 模型:一个主体 + 一个helper. 对于一个规模N的问题, 寻找所有0->N的解
# 在helper里描述每一步的所有情况, 例如: 左 < 右; 左 = 右 = 0; 左 > 右
# 存在一种情况, 减小了问题规模, 但是解决办法还是相同的helper. 大 => 小

class Solution:
  def generateParenthesis(self, n):
    res = []
    if n < 1:
      return res
    self.helper(res, "", n, n)
    return res

  def helper(self, res, path, left, right):
    if right < left:
      return
    if left == 0 and right == 0:
      res.append(path)
      return
    if left > 0:
      self.helper(res, path + "(", left - 1, right)
    if right > 0:
      self.helper(res, path + ")", left, right - 1)