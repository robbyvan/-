# 354_Russian Doll Envelopes
# 排序 + LIS
# s = sorted(envelopes, key = lambda x: (x[0], -x[1])) 再二分LIS

class Solution:
  def maxEnvelopes(self, envelopes):
    def comp(x, y):
      return -1 if (x[0] < y[0] or x[0] == y[0] and x[1] > y[1]) else 1

    def findLIS(envs):
      tails = [0] * len(envs)
      size = 0
      for item in envs:
        l, r = 0, size
        while l < r:
          m = l + (r - l) // 2
          if tails[m] < item[1]:
            l = m + 1
          else:
            r = m
        tails[l] = item[1]
        size = max(size, l + 1)
      return size

    if not envelopes:
      return 0
    envelopes.sort(cmp = comp)
    return findLIS(envelopes)

  

  



# O(n^2)
# class Solution:
#   def maxEnvelopes(self, envelopes):
#     if not envelopes:
#       return 0
#     envelopes = sorted(envelopes, key = lambda item: item[0])
#     dp = [1 for _ in range(len(envelopes))]

#     maxDoll = 1
#     for i in range(1, len(envelopes)):
#       dp[i] = 1
#       for j in range(i - 1, -1, -1):
#         if envelopes[j][0] < envelopes[i][0] and envelopes[j][1] < envelopes[i][1]:
#           dp[i] = max(dp[i], dp[j] + 1)
#       maxDoll = max(maxDoll, dp[i])
#     return maxDoll

a = Solution().maxEnvelopes([[1,3],[3,5],[6,7],[6,8],[8,4],[9,5]])
print(a)