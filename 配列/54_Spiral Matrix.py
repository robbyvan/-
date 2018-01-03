# 54_Spiral Matrix
# 按照定义
# 上pop(0)
# 右row.pop()
# 下matrix.pop()[::-1]
# 左row.pop(0)

class Solution:
  def spiralOrder(self, matrix):
    if not matrix or not matrix[0]:
      return []
    res = []
    while matrix:
      res += matrix.pop(0)
      if matrix and matrix[0]:
        for row in matrix:
          res.append(row.pop())
      if matrix:
        res += matrix.pop()[::-1]
      if matrix and matrix[0]:
        for row in matrix[::-1]:
          res.append(row.pop(0))
    return res