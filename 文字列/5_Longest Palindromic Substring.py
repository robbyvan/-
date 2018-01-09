# 5_Longest Palindromic Substring
# 1) 考虑dp[i][j]就是s[i:j+1], 递推dp[i][j] = (s[i] == s[j]) and j - i < 2 or dp[i + 1][j - 1]
# 因为有j - i < 2的存在, 所以不需要补行列△
# 2) 每个点奇偶expand, 检查是否满足.

class Solution:
  def longestPalindrome(self, s):
    start, end = 0, 0
    dp = [[False for j in range(len(s))] for i in range(len(s))]
    for j in range(len(s)):
      for i in range(j, -1, -1):
        dp[i][j] = (s[i] == s[j]) and (j - i < 2 or dp[i + 1][j - 1])
        if dp[i][j] and end - start < j - i:
          start, end = i , j

    return s[start:end + 1]

# class Solution:
#   def longestPalindrome(self, s):
#     res = ""
#     for i in range(len(s)):
#       temp = self.helper(s, i, i)
#       if len(temp) > len(res):
#         res = temp
#       temp = self.helper(s, i, i + 1)
#       if len(temp) > len(res):
#         res = temp
#     return res
#   def helper(self, s, l, r):
#     while l >= 0 and r < len(s) and s[l] == s[r]:
#       l -= 1, r += 1
#     return s[l + 1: r]