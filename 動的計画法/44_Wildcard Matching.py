# 44_Wildcard Matching

class Solution:
  def isMatch(self, s, p):
    m, n = len(s), len(p)
    dp = [ [False] * (n + 1) for _ in range(m + 1) ]

    dp[0][0] = True
    for j in range(n):
      if p[j] == "*":
        dp[0][j + 1] = dp[0][j]

    for i in range(m):
      for j in range(n):
        if p[j] == "?" or p[j] == s[i]:
          dp[i + 1][j + 1] = dp[i][j]
        if p[j] == "*":
          dp[i + 1][j + 1] = dp[i][j + 1] or dp[i + 1][j]

    return dp[-1][-1]