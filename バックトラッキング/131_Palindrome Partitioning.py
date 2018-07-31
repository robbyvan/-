# 131_Palindrome Partitioning
# 1) DP.
# 2) 类似word break. top-down.解决[0, n] 可以从n下的所有尾部回文得出.
# f(n) = f(n - k) + s[n - k:]
#         所有答案      是回文

# class Solution:
#   def partition(self, s):
#     self.memo = {}
#     return self.helper(s, len(s) - 1)

#   def helper(self, s, index):
#     if index < 0:
#       return []
#     if index in self.memo:
#       return self.memo[index]
#     res = []
#     for left in range(index, -1, -1):
#      curr = s[left:index + 1]
#      if self.isPalindome(curr):
#       if left == 0:
#         res.append([curr])
#       else:
#           prev = self.helper(s, left - 1)
#           for p in prev:
#             res.append(p + [curr])
#     self.memo[index] = res
#     return res

#   def isPalindome(self, s):
#     if len(s) < 2:
#       return True
#     l, r = 0, len(s) - 1
#     while l < r:
#       if s[l] != s[r]:
#         return False
#       l += 1
#       r -= 1
#     return True

class Solution:
  def partition(self, s):
    n = len(s)
    res = [[]] * n
    dp = [[False] * n for _ in range(n)]

    for j in range(n):
      ans = []
      for i in range(j, -1, -1):
        if s[i] == s[j] and (j - i < 2 or dp[i + 1][j - 1]):
          dp[i][j] = True
          if i == 0:
            ans += [[s[i:j + 1]]]
          elif i > 0:
            ans += [ prev + [s[i:j + 1]] for prev in res[i - 1]]
      res[j] = ans

    return res[-1]

a = Solution().partition("aab")
print(a)