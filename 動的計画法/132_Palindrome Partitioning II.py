# 132_Palindrome Partitioning II
# 同131, 只用记录mincut即可

class Solution:
  def minCut(self, s):
    n = len(s)
    opt = [[False] * n for _ in range(n)]
    dp = [-1] * (n + 1)

    for i in range(1, n + 1):
      dp[i] = i - 1

    for j in range(n):
      for i in range(j, -1, -1):
        if s[i] == s[j] and (j - i < 2 or opt[i + 1][j - 1]):
          opt[i][j] = True
          dp[j + 1] = min(dp[i] + 1, dp[j + 1])

    return dp[n]


# class Solution:
#   def minCut(self, s):
#     n = len(s)
#     dp = [[False] * n for _ in range(n)]
#     minCuts = [[]] * (n + 1)
#     res = list(s)

#     for j in range(n):
#       ans = list(s[:j + 1])
#       for i in range(j, -1, -1):
#         if s[i] == s[j]:
#           if j - i < 2:
#             dp[i][j] = True
#           else:
#             dp[i][j] = dp[i + 1][j - 1]
#           if dp[i][j]:
#             newCut = minCuts[i] + [s[i: j + 1]]
#             if len(newCut) < len(ans):
#               ans = newCut
#       minCuts[j + 1] = ans

#     return len(minCuts[-1]) - 1

