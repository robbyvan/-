# 52_N-Queens II
# 同51, 不必记录path

class Solution:
  def totalNQueens(self, n):
    if n < 1:
      return 0
    res = [0]
    self.helper(n, 0, [], [], [], res)
    return res[0]

  def helper(self, n, i, invalidSum, invalidDiff, invalidCols, res):
    if i == n:
      res[0] += 1
      return

    for j in range(n):
      if j in invalidCols:
        continue
      if (i + j) not in invalidSum and (j - i) not in invalidDiff:
        self.helper(n, i + 1, invalidSum + [i + j], invalidDiff + [j - i], invalidCols + [j], res)
      

a = Solution().totalNQueens(4)
print(a)