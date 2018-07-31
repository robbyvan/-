# 51_N-Queens
# 限制规则: 不在之前皇后的y = x和y = -x 以及行列上
# 行列限制: 每次在新的一行取, [取过的列], [y = x], [y = -x]检查
# 画棋盘: 皇后坐标 => 2D矩阵

class Solution:
  def solveNQueens(self, n):
    res = []
    self.helper(n, 0, [], [], [], [], res)
    return self.drawBoard(n, res)

  def helper(self, n, i, invalidSum, invalidDiff, invalidCols, path, res):
    if i == n:
      res.append(path)
      return
    for j in range(n):
      if j in invalidCols:
        continue
      if (i + j) not in invalidSum and (j - i) not in invalidDiff:
        self.helper(n, i + 1, invalidSum + [i + j], invalidDiff + [j - i], invalidCols + [j], path + [j], res)

  def drawBoard(self, n, res):
    if len(res) == 0:
      return []
    ans = []
    for solution in res:
      board = []
      row = "." * n
      for queenCol in solution:
        board.append(row[:queenCol] + "Q" + row[queenCol + 1:])
      ans.append(board)
    return ans

a = Solution().solveNQueens(4)
print(a)