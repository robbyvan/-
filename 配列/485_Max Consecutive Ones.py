# 485. Max Consecutive Ones
# 分段数, 每次遇到0更新max
class Solution:
  def findMaxConsecutiveOnes(self, nums):
    count, res = 0, 0
    for num in nums:
      if num == 1:
        count += 1
        res = max(res, count)
      else:
        count = 0
    return res