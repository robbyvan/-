# 97_Interleaving String
# DP 考虑s1[0:i] s2[0:j] => s1[0:i] s2[0:j + 1]
# 找递推公式 按照意义找.
# 递推公式dp[i][j] = dp[i][j - 1] and s2[j - 1] == s3[i + j - 1] or dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]
# 补行△1列△2, 初始化空串 for i in range(r), i是字符串指针, dp[i + 1][0] = dp[i][0] and s1[i] == s3[i]
# 开始循环按照字符串i, j遍历, 配合△1 △2调整递推公式.

class Solution:
  def isInterleave(self, s1, s2, s3):
    r, c, l = len(s1), len(s2), len(s3)
    if r + c != l:
      return False
    dp = [[True for _ in range(c + 1)] for _ in range(r + 1)]
    for i in range(r):
      dp[i + 1][0] = dp[i][0] and s1[i] == s3[i]
    for j in range(c):
      dp[0][j + 1] = dp[0][j] and s2[j] == s3[j]
    for i in range(r):
      for j in range(c):
        dp[i + 1][j + 1] = dp[i + 1][j] and s2[j] == s3[i + j + 1] or dp[i][j + 1] and s1[i] == s3[i + j + 1]
    return dp[-1][-1]
