# 90_Subsets II

class Solution:
  def subsetsWithDup(self, nums):
    res = []
    nums.sort()
    self.helper(nums, 0, [], res)
    return res

  def helper(self, source, index, path, res):
    res.append(path)
    for i in range(index, len(source)):
      if i > index and source[i] == source[i - 1]:
        continue
      self.helper(source, i + 1, path + [source[i]], res)

# class Solution:
#   def subsetsWithDup(self, nums):
#     res = []
#     nums.sort()
#     for k in range(len(nums) + 1):
#       self.helper(nums, k, [], res)
#     return res

#   def helper(self, source, n, path, res):
#     if n == 0:
#       res.append(path)
#       return 

#     used = set()
#     for i in range(len(source)):
#       if source[i] not in used:
#         used.add(source[i])
#         if len(source[i + 1:]) >= n - 1:
#           self.helper(source[i + 1:], n - 1, path + [source[i]], res)
