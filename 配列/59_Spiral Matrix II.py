# 59_Spiral Matrix II
# 按定义, 四个边界walk. while top <= bot and left <= right

class Solution:
  def generateMatrix(self, n):
    res = [[0 for _ in range(n) ] for _ in range(n)]
    top, bot, left, right = 0, n - 1, 0, n - 1
    num = 1
    while top <= bot and left <= right:
      for j in range(left, right + 1):
        res[top][j] = num
        num += 1
      top += 1
      for i in range(top, bot + 1):
        res[i][right] = num
        num += 1
      right -= 1
      for j in range(right, left - 1, -1):
        res[bot][j] = num
        num += 1
      bot -= 1
      for i in range(bot, top - 1, -1):
        res[i][left] = num
        num += 1
      left += 1
    return res