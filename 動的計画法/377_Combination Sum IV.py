# 377_Combination Sum IV
# hash表dp, 找差值, 类似coin, 但是coin求coin个数, 这里求组合数

class Solution:
  def combinationSum4(self, nums, target):
    if target < 0:
      return 0
    d = {}
    d[0] = 0
    d[target] = 0
    for num in nums:
      d[num] = 1
    for i in range(1, target + 1):
      for num in nums:
        if i - num >= 0:
          if (i - num) in d:
            d[i] = d.get(i, 0) + d[i - num]
    return d[target]

a = Solution().combinationSum4([1, 2, 3], 4)
print(a)