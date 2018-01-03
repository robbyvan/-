# 78. Subsets
# 递归: 从1 -> n 含i的所有解
# 迭代: 每当遇到新的i, 添加进去含i与之前的组合的解.

#递归
class Solution:
  def subsets(self, nums):
    res = []
    self.dfs(nums, 0, [], res)
    return res

  def dfs(self, nums, index, path, res):
    res.append(path)
    for i in range(index, len(nums)):
      self.dfs(nums, i + 1, path + [nums[i]], res)

# 迭代
# class Solution:
#   def subsets(self, nums):
#     res = [[]]
#     for num in nums:
#       res += [item + [num] for item in res]
#     return res