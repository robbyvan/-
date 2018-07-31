# 139_Word Break
# DP解决. dp[i] = { (s[i + 1 - lw : i + 1] == w) and (dp[i - lw] or i - lw + 1 == 0) } 所有w求or

class Solution:
  def wordBreak(self, s, wordDict):
    dp = [False] * len(s)

    for i in range(len(s)):
      for word in wordDict:
        if s[i + 1 - len(word): i + 1] == word and (dp[i - len(word)] or i + 1 - len(word) == 0):
          dp[i] = True
          break

    return dp[-1]

# class Solution:
#   def wordBreak(self, s, wordDict):
#     dp = [False] * len(s)

#     for i in range(len(s)):
#       for word in wordDict:
#         if i + 1 - len(word) == 0:
#           dp[i] = dp[i] or (word == s[i + 1 - len(word) : i + 1])
#         elif i + 1 - len(word) > 0:
#           dp[i] = dp[i] or dp[i - len(word)] and (word == s[i + 1 - len(word) : i + 1])

#     return dp[-1]