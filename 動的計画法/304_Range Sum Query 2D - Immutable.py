# 304_Range Sum Query 2D - Immutable
# 笛卡尔

class NumMatrix(object):
  def __init__(self, matrix):
    m = len(matrix)
    if not m:
      return None
    n = len(matrix[0])
    if not n:
      return None
    self.dp = [ [0] * (n + 1) for _ in range(m + 1) ]
    self.dp[1][1] = matrix[0][0]
    for i in range(1, m + 1):
      for j in range(1, n + 1):
        self.dp[i][j] = matrix[i - 1][j - 1] + self.dp[i - 1][j] + self.dp[i][j - 1] - self.dp[i - 1][j - 1]

  def sumRegion(self, row1, col1, row2, col2):
    row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
    return self.dp[row2][col2] - self.dp[row1 - 1][col2] - self.dp[row2][col1 - 1] + self.dp[row1 - 1][col1 - 1]