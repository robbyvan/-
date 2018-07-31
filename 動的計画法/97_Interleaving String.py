# 97_Interleaving String
# dp[i + 1][j + 1] = dp[i + 1][j] and s3[i + j - 1] == s2[j] or dp[i][j + 1] and s3[i + j - 1] == s1[i]
# 注意公式里字符串坐标也跟着变化了.

class Solution:
  def isInterleave(self, s1, s2, s3):
    m, n, l = len(s1), len(s2), len(s3)
    if m + n != l:
      return False
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True
    for i in range(m):
      dp[i + 1][0] = dp[i][0] and s3[i] == s1[i]
    for j in range(n):
      dp[0][j + 1] = dp[0][j] and s3[j] == s2[j]
    for i in range(m):
      for j in range(n):
        dp[i + 1][j + 1] = dp[i + 1][j] and s3[i + j - 1] == s2[j] or dp[i][j + 1] and s3[i + j - 1] == s1[i]
    return dp[-1][-1]