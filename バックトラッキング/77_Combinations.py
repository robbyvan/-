# 77_Combinations
# dfs + memo
# 去重: 每下次组合只能选择从比这次的数字更大的中挑选.

class Solution:
  def combine(self, n, k):
    self.memo = {}
    return self.helper(tuple(range(1, n + 1)), k)

  def helper(self, source, k):
    key = (source, k)
    if key in self.memo:
      return self.memo[key]
    if k == 0:
      return [[]]
    ans = []
    for i in range(len(source)):
      main = source[i]
      others = self.helper(source[i + 1:], k - 1)
      ans += [[main] + res for res in others]
    self.memo[key] = ans
    return ans

# class Solution:
#   def combine(self, n, k):
#     res = []
#     self.helper(range(1, n + 1), 0, k, [], res)
#     return res

#   def helper(self, source, index, k, path, res):
#     if k == 0:
#       res.append(path)
#       return

#     for i in range(index, len(source)):
#       self.helper(source, i + 1, k - 1, path + [source[i]], res)