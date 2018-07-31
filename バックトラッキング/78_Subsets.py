# 78_Subsets
# 1) DP: 因为是set, 每多一个数字, 在之前的答案上添加即可
# 2) DFS: helper(n): 从nums的大小为n的子集 => 去重: 要求每次取后, 下次(之后的栈)只能在原source[i]之后取, 所以用len(source[i + 1:]) >= n - 1)剪枝

# class Solution:
#   def subsets(self, nums):
#     res = [[]]
#     for num in nums:
#       res += [prev + [num] for prev in res]
#     return res

class Solution:
  def subsets(self, nums):
    res = []
    for k in range(len(nums) + 1):
      self.helper(nums, k, [], res)
    return res

  def helper(self, source, n, path, res):
    if n == 0:
      res.append(path)
      return

    for i in range(len(source)):
      if (len(source[i + 1:]) >= n - 1):
        self.helper(source[i + 1:], n - 1, path + [source[i]], res)