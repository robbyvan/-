# 216. Combination Sum III
# 回溯
# 去重: 本身unique, 每次用掉一个后修改candidates数组(删掉, 可用filter)
class Solution(object):
  def combinationSum3(self, k, n):
    if k > 9:
      return []
    candidates = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    res = []
    self.dfs(candidates, k, n, [], res)
    return res
  def dfs(self, candidates, steps, target, path, res):
    if target < 0 or steps < 0:
      return
    if target == 0 and steps == 0:
      res.append(path)
      return
    for i in range(len(candidates)):
      newCandidates = filter(lambda x: x > candidates[i], candidates)
      self.dfs(newCandidates, steps - 1, target - candidates[i], path + [candidates[i]], res)