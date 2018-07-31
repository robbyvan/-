# 5_Longest Palindromic Substring
# 见字符串5
# 区别subsequence 和 substring!
# DP含义: (i, j) 是不是回文 => 计算的同时更新[start, end]

class Solution:
  def longestPalindrome(self, s):
    if len(s) < 1:
      return 0
    n = len(s)
    dp = [[False] * n  for _ in range(n)]
    start, end = 0, 0
    for j in range(n):
      for i in range(j, -1, -1):
        if s[i] == s[j]:
          if j - i < 2:
            dp[i][j] = True
          else:
            dp[i][j] = dp[i + 1][j - 1]
        if dp[i][j] and j - i > end - start:
          start, end = i, j
    return s[start:end + 1]