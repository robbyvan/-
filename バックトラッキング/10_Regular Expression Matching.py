# 10_Regular Expression Matching
# 1) dp, 参见字符串10
# 2) 回溯.


# class Solution:
#   def isMatch(self, s, p):

#     m, n = len(s), len(p)
#     dp = [[False] * (n + 2) for _ in range(m + 1)]

#     dp[0][0] = True
#     dp[0][1] = True
#     for j in range(n):
#       if p[j] == "*":
#         dp[0][j + 2] = dp[0][j]

#     for i in range(m):
#       for j in range(n):
#         if p[j] == "." or p[j] == s[i]:
#           dp[i + 1][j + 2] = dp[i][j + 1]
#         if p[j] == "*":
#           if p[j - 1] == s[i] or p[j - 1] == ".":
#             dp[i + 1][j + 2] = dp[i][j + 2] or dp[i + 1][j + 1] or dp[i  + 1][j]
#           else:
#             dp[i + 1][j + 2] = dp[i + 1][j]

#     return dp[-1][-1]