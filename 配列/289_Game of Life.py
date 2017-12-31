# 289. Game of Life
# 利用2进制保存两个状态00 01 10 11
# 下个状态生就+2(+10)
# 检查相邻注意边界, 使用max min
class Solution:
  def gameOfLife(self, board):
    if not board or not board[0]:
      return None

    m, n = len(board), len(board[0])
    for i in range(m):
      for j in range(n):
        self.update(board, m, n, i, j)

    for i in range(m):
      for j in range(n):
        board[i][j] = board[i][j] >> 1

  def update(self, board, m, n, i, j):
    live = 0
    for p in range(max(i - 1, 0), min(i + 2, m)):
      for q in range(max(j - 1, 0), min(j + 2), n):
        live += board[p][q] & 1
    if live == 3 or live == board[i][j] + 3:
      board[i][j] += 2