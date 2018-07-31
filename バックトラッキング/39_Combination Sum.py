# 39_Combination Sum
# 去重? dfs不存在重复. 因为candidates是唯一的.
# sort只是为了加快速度罢了.

class Solution:
  def combinationSum(self, candidates, target):
    candidates.sort()
    res = []
    self.helper(candidates, 0, target, [], res)
    return res

  def helper(self, candidates, index, target, path, res):
    if target == 0:
      res.append(path)
      return
    for i in range(len(candidates) - 1, index - 1, -1):
      if target - candidates[i] >= 0:
        self.helper(candidates, i, target - candidates[i], path + [candidates[i]], res)

a = Solution().combinationSum([2, 3, 6, 7], 7)
print(a)