# 72_Edit Distance
# DP, 类似subsequence, 比较末位
# 如果末位相同, dp[i + 1][j + 1] = dp[i][j]
# 否则取三种变化步数最小: min(dp[i][j], dp[i][j + 1], dp[i + 1][j]) + 1
# 如果添加了行列△, 初始化的时候也要包括新增行列: for i in range(m + 1)

class Solution:
  def minDistance(self, word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(m + 1):
      dp[i][0] = i
    for j in range(n + 1):
      dp[0][j] = j
    for j in range(n):
      for i in range(m):
        if word1[i] == word2[j]:
          dp[i + 1][j + 1] = dp[i][j]
        else:
          dp[i + 1][j + 1] = min(dp[i][j], dp[i][j + 1], dp[i + 1][j]) + 1
    return dp[-1][-1]
