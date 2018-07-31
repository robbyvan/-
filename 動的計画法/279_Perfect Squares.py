# 279_Perfect Squares
# 1.找硬币DP, opt(k, target) = min(opt(k - 1, target), opt(k, target - Vk) + 1)
# 与416的区别: 基本硬币面额可以重复使用, 所以是opt(k, target - Vk) + 1; 背包问题, 物品只有一个, 选择后就没有了
# 2.BFS, 每次扫描所有的硬币, 确定下次开始找零金额

class Solution:
  def numSquares(self, n):
    if n < 2:
      return n
    i, coins = 1, []
    while i * i <= n:
      coins.append(i)
      i += 1
    q, count = set(), 0
    q.add(n)
    while q:
      count += 1
      nextQ = set()
      for target in q:
        for coin in coins:
          if target == coin:
            return count
          if target > coin:
            nextQ.add(target - coin)
      q = nextQ 
    return count




# class Solution:
#   def numSquares(self, n):
#     coins = []
#     i = 1
#     while i * i <= n:
#       coins += [i * i]
#       i += 1
#     m = len(coins)
#     dp = [[float("inf")] * (n + 1) for _ in range(m + 1)]

#     for k in range(m + 1):
#       dp[k][0] = 0
#     for t in range(1, n + 1):
#       dp[1][t] = t

#     for k in range(2, m + 1):
#       for t in range(1, n + 1):
#         if t >= coins[k - 1]:
#           dp[k][t] = min(dp[k - 1][t], dp[k][t - coins[k - 1]] + 1)
#         else:
#           dp[k][t] = dp[k - 1][t]
#     print(dp)
#     return dp[m][n]

# a = Solution().numSquares(8)
# print(a)