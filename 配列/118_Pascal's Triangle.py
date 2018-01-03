# 118_Pascal's Triangle
# 新的row由row - 1的内容得到.
class Solution:
  def generate(self, numRows):
    if numRows < 1:
      return []
    if numRows == 1:
      return [[1]]
    if numRows == 2:
      return [[1], [1, 1]]
    res = [[1], [1, 1]]
    for row in range(3, numRows + 1):
      path = []
      for i in range(len(res[-1])):
        if i == 0:
          path.append(1)
        else:
          path.append(res[-1][i] + res[-1][i - 1])
      path.append(1)
      res.append(path)
    return res
