# 73_Set Matrix Zeroes
# 利用第一行, 第一列记录从1,1到m, n之间的内容是否让此行/列成为0
# 但是有可能第一行列存在0, 因此利用两个变量记录是否有这种情况
# 上述扫描完成后, 根据第一行列/两个变量进行置零

class Solution:
  def setZeroes(self, matrix):
    m = len(matrix)
    if m == 0:
      return
    n = len(matrix[0])

    colHasZero = False
    for i in range(m):
      if matrix[i][0] == 0:
        colHasZero = True
        break

    rowHasZero = False
    for j in range(n):
      if matrix[0][j] == 0:
        rowHasZero = True
        break

    for i in range(1, m):
      for j in range(1, n):
        if matrix[i][j] == 0:
          matrix[i][0] = 0
          matrix[0][j] = 0

    for i in range(1, m):
      if matrix[i][0] == 0:
        for j in range(1, n):
          matrix[i][j] = 0

    for j in range(1, n):
      if matrix[0][j] == 0:
        for i in range(1, m):
          matrix[i][j] = 0

    if rowHasZero:
      for j in range(n):
        matrix[0][j] = 0
    if colHasZero:
      for i in range(m):
        matrix[i][0] = 0


