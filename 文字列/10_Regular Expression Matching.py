# 10_Regular Expression Matching
# 利用dp, 如果是简单的尾=尾, 或者p是'.', [i, j] = [i - 1, j - 1]
# 如果p是'*', 考虑"*"之前一位是否相等. 如果不等, 则扔掉这两位[i, j] = [i, j - 2]
# 如果相等.考虑0, 1, 多
# 0 => [i, j] = [i, j - 2]
# 1 => [i, j] = [i, j - 1]
# 多 => 说明i比j多, 则扔掉一个s的末位, 假设匹配了.
# (如果之前就不能做到匹配, 多一位反而匹配不可能; 如果之前能匹配, 一定末位是相同且*利用了, 否则j消掉两个还能匹配说明i比j短, 与之前i比j长扔了i矛盾了)
# 所以只要考虑[i, j] = [i - 1, j]即可

class Solution:
  def isMatch(self, s, p):
    dp = [[False for _ in range(len(p) + 2)] for _ in range(len(s) + 1)]
    dp[0][0] = True
    dp[0][1] = True
    for j in range(len(p)):
      if p[j] == '*':
        dp[0][j + 2] = dp[0][j]

    for i in range(len(s)):
      for j in range(len(p)):
        if p[j] == s[i] or p[j] == '.':
          dp[i + 1][j + 2] = dp[i][j + 1]
        if p[j] == '*':
          if p[j - 1] != s[i] and p[j - 1] != '.':
            dp[i + 1][j + 2] = dp[i + 1][j]
          else:
            dp[i + 1][j + 2] = dp[i + 1][j] or dp[i + 1][j + 1] or dp[i][j + 2]

    return dp[-1][-1]
