# 221_Maximal Square
# if matrix[i][j] == "1": => dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1
# 退化m * n的dp表 => 只需要2行(或2列)

class Solution:
  def maximalSquare(self, matrix):
    if not matrix:
      return 0
    m, n = len(matrix), len(matrix[0])
    if not n:
      return 0

    cur, pre = [0] * n, [0] * n
    maxSize = 0
    for j in range(n):
      pre[j] = 0 if matrix[0][j] == "0" else 1
      maxSize = max(maxSize, pre[j])

    for i in range(1, m):
      cur[0] = 0 if matrix[i][0] == "0" else 1
      maxSize = max(maxSize, cur[0])
      for j in range(1, n):
        if matrix[i][j] == "1":
          cur[j] = min(cur[j - 1], pre[j - 1], pre[j]) + 1
          maxSize = max(maxSize, cur[j])
      pre, cur = cur, [0] * n

    return maxSize * maxSize
  
# class Solution:
#   def maximalSquare(self, matrix):
#     if not matrix:
#       return 0
#     m, n = len(matrix), len(matrix[0])
#     if not n:
#       return 0
#     pre, cur = [0] * m, [0] * m
#     maxSize = 0
#     for i in range(m):
#       pre[i] = 0 if matrix[i][0] == "0" else 1
#       maxSize = max(maxSize, pre[i])

#     for j in range(1, n):
#       cur[0] = 0 if matrix[0][j] == "0" else 1
#       maxSize = max(maxSize, cur[0])
#       for i in range(1, m):
#         if matrix[i][j] == "1":
#           cur[i] = min(pre[i], cur[i - 1], pre[i - 1]) + 1
#           maxSize = max(maxSize, cur[i])
#       pre = cur
#       cur = [0] * m
#     return maxSize * maxSize



# class Solution:
#   def maximalSquare(self, matrix):
#     if not matrix:
#       return 0
#     m, n = len(matrix), len(matrix[0])
#     if n == 0:
#       return 0
#     dp = [[0] * n for _ in range(m)]
#     maxSize = 0
#     for i in range(m):
#       dp[i][0] = 1 if matrix[i][0] == "1" else 0
#       maxSize = max(maxSize, dp[i][0])
#     for j in range(n):
#       dp[0][j] = 1 if matrix[0][j] == "1" else 0
#       maxSize = max(maxSize, dp[0][j])
#     for i in range(1, m):
#       for j in range(1, n):
#         if matrix[i][j] == "1":
#           dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1
#           maxSize = max(maxSize, dp[i][j])
#     return maxSize * maxSize
