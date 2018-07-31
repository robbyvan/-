# 10_Regular Expression Matching
# dp[0][0] = True
# dp[0][1] = True  => why? 因为j补了两列, 对于p[j]中的j = 0, 对应的是dp: 1个字符, 所以dp中的0个字符有: j = 0, 1(因为是减2的关系, 初始化两个基准)

class Solution:
  def isMatch(self, s, p):
    m, n = len(s), len(p)
    dp = [ [False] * (n + 2) for _ in range(m + 1)]

    dp[0][0] = True
    dp[0][1] = True
    for j in range(1, n):
      if p[j] == "*":
        dp[0][j + 2] = dp[0][j]

    for i in range(m):
      for j in range(n):
        if s[i] == p[j] or p[j] == ".":
          dp[i + 1][j + 2] = dp[i][j + 1]
        if p[j] == "*":
          if s[i] == p[j - 1] or p[j - 1] == ".":
            dp[i + 1][j + 2] = dp[i + 1][j] or dp[i + 1][j + 1] or dp[i][j + 2]
          else:
            dp[i + 1][j + 2] = dp[i + 1][j]

    return dp[-1][-1]