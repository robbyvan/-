# 90. Subsets II
# dfs: 从某个点开始找到一条到结尾的路
# [1, 2, 2]实际顺序: 1, 12, 122, 12, 122, 2, 22
# 但是因为有重复, 因此在回退的时候(发现第二个2和删掉的第一个2是相同, 因此应该跳过第二个2)
# 所以if i > index(保证有i - 1) and nums[i] == nums[i - 1]就continue


class Solution:
  def subsetsWithDup(self, nums):
    res = []
    nums.sort()
    self.dfs(nums, 0, [], res)
    return res

  def dfs(self, nums, index, path ,res):
    res.append(path)
    for i in range(index, len(nums)):
      if i > index and nums[i] == nums[i - 1]:
        continue
      self.dfs(nums, i + 1, path + [nums[i]], res)