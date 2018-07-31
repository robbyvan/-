# 37_Sudoku Solver
# main: 解决 => 填字(反复调用自身填字) => 所有填字操作都在同一个self.board上操作
# 填字? => 找空格(填完了, 结束) => 选择合适的数字填入(校验) 
# 找空格 => 扫到第一个"."
# 校验 => 检查row, col, cell
# 尝试填一个字, 调用自身(检查返回的bool === 更小规模的问题能否解决) => 根据结果返回true, false

class Solution:
  def solveSudoku(self, board):
    self.board = board
    self.solve()

  def findToFill(self):
    for row in range(9):
      for col in range(9):
        if self.board[row][col] == ".":
          return row, col
    return -1, -1

  def solve(self):
    row, col = self.findToFill()
    if row == -1 and col == -1:
      return True
    for num in [str(i) for i in range(1, 10)]:
      if self.isSafe(row, col, num):
        self.board[row][col] = num
        if self.solve():
          return True
        self.board[row][col] = "."
    return False

  def isSafe(self, row, col, ch):
    boxrow = row - row % 3
    boxcol = col - col % 3
    if self.checkrow(row,ch) and self.checkcol(col,ch) and self.checksquare(boxrow, boxcol, ch):
        return True
    return False

  def checkrow(self, row, ch):
    for col in range(9):
      if self.board[row][col] == ch:
        return False
    return True

  def checkcol(self, col, ch):
    for row in range(9):
      if self.board[row][col] == ch:
        return False
    return True

  def checksquare(self, row, col, ch):
    for r in range(row, row+3):
      for c in range(col, col+3):
        if self.board[r][c] == ch:
          return False
    return True
