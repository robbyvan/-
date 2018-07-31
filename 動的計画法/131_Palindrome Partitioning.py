# 131_Palindrome Partitioning
# 1.DFS
# 2.DP: 类似longest palindrome算法, 每次扩大j, 对每个j的所有i, 如果遇到(i, j)是回文
# 组合[0, i)内的所有已知答案(all in dp[i - 1]) + s[i, j], 保存到dp[j]
# => 两个dp表: 真值表dp + 答案dp

class Solution:
  def partition(self, s):
    n = len(s)
    prev = [[[]]] * (n + 1)
    dp = [[False] * n for _ in range(n)]

    for j in range(n):
      ans = []
      for i in range(j, -1, -1):
        if s[i] == s[j]:
          if j - i < 2:
            dp[i][j] = True
          else:
            dp[i][j] = dp[i + 1][j - 1]
        if dp[i][j]:
          ans += [l + [s[i: j + 1]] for l in prev[i]]
      prev[j + 1] = ans

    return prev[-1]
      
a = Solution().partition("aab")
print(a)





# class Solution:
#   def partition(self, s):
#     res = []
#     self.dfs(s, [], res)
#     return res

#   def dfs(self, s, path, res):
#     if not s:
#       res.append(path)
#       return
#     for cut in range(1, len(s) + 1):
#       if self.isPalinrome(s[:cut]):
#         self.dfs(s[cut:], path + [s[:cut]], res)

#   def isPalinrome(self, s):
#     if not s:
#       return True
#     l, r = 0, len(s) - 1
#     while l < r:
#       if s[l] != s[r]:
#         return False
#       l, r = l + 1, r - 1
#     return True