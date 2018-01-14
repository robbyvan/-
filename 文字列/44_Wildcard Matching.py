# 44_Wildcard Matching
# 类似第10题, 但是这里的*和前一个字符无关.
# 所以*时, dp[i][j] = dp[i][j - 1](看做空) or dp[i - 1][j]匹配当前.
# 初始化时, 初始化s = 0, p in range(n)的情况, 考虑当前是否是"*"
# 如果是"*", dp[0][j] = dp[0][j - 1]; 否则False

class Solution:
  def isMatch(self, s, p):
    m, n = len(s), len(p)
    dp = [[False for _ in range(n + 1)] for _ in range(m + 1)]
    dp[0][0] = True
    for j in range(n):
      if p[j] == "*":
        dp[0][j + 1] = dp[0][j]
      else:
        dp[0][j + 1] = False
    for i in range(m):
      for j in range(n):
        if s[i] == p[j] or p[j] == "?":
          dp[i + 1][j + 1] = dp[i][j]
        elif p[j] == "*":
          dp[i + 1][j + 1] = dp[i + 1][j] or dp[i][j + 1]
    return dp[-1][-1]
