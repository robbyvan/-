# 115_Distinct Subsequences
# 最后要求解s[0:m]和t[0:n]的sub sequence. 考虑[0:i]和[0:j]的匹配问题
# 如果s[i] == t[j], 那么dp[i][j]可能是s[0:i-1]和t[0:j-1], 也可能不要这个相等的s[i], 还是s[0:i-1]和t[0:j]
# 所以相等时dp[i + 1][j + 1] = dp[i][j + 1] + dp[i][j]
# 不等时, 同上2情况, 扔掉s[i], dp[i + 1][j + 1] = dp[i][j + 1]
# 对于dp问题, 循环时, 以字符串的index为准设置i, j. 根据递推公式补行△1 列△2, 根据补了行列的数目调整求解dp[p][q]的p, q
# 一般是p = i + △1, q = j + △2

class Solution:
  def numDistinct(self, s, t):
    m, n = len(s), len(t)
    if m < n:
      return 0
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(m + 1):
      dp[i][0] = 1
    for j in range(n):
      for i in range(j, m):
        if t[j] == s[i]:
          dp[i + 1][j + 1] = dp[i][j + 1] + dp[i][j]
        else:
          dp[i + 1][j + 1] = dp[i][j + 1]
    return dp[-1][-1]
