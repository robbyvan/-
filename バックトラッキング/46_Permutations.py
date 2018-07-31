# 46_Permutations
# 就基础的DFS即可

class Solution:
  def permute(self, nums):
    if not nums:
      return []
    res = []
    self.helper(nums, [], res)
    return res

  def helper(self, source, path, res):
    if not source:
      res.append(path)
      return

    for i in range(len(source)):
      self.helper(source[:i] + source[i + 1:], path + [source[i]], res)