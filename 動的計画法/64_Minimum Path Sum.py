# 64_Minimum Path Sum
# 见数组64
# 关于dp初始化的△? 
# 先看递推公式, 再看初始化, 再看本体循环, 如果还有越界, 才考虑补充△ + 替换i, j

class Solution:
  def minPathSum(self, grid):
    m, n = len(grid), len(grid[0])
    opt = [[0] * (n) for _ in range(m)]
    opt[0][0] = grid[0][0]

    for j in range(1, n):
      opt[0][j] = opt[0][j - 1] + grid[0][j]
    for i in range(1, m):
      opt[i][0] = opt[i - 1][0] + grid[i][0]

    for i in range(1, m):
      for j in range(1, n):
        opt[i][j] = min(opt[i - 1][j], opt[i][j - 1]) + grid[i][j]

    return opt[-1][-1]