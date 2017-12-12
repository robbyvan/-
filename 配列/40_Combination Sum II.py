# 40. Combination Sum II
# 相同回溯
# 去重: sort + 循环跳过nums[i] == nums[i-1]的情况. (要求选中的每一个数字不能和之前的重复)
class Solution:
  def combinationSum2(self, candidates, target):
    candidates.sort()
    res = []
    self.dfs(candidates, target, 0, [], res)
    return res
  def dfs(self, candidates, target, index, path, res):
    if target < 0:
      return
    if target == 0:
      res.append(path)
      return
    for i in range(index, len(candidates)):
      if i != index and candidates[i] == candidates[i - 1]:
        continue
      self.dfs(candidates, target - candidates[i], i + 1, path + [candidates[i]], res)
