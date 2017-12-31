# 55. Jump Game
# 遍历一次, 利用maxRange记住当前最远位置
# 遍历的时候先检查该位置能否达到: 比较index和maxRange
# 每次更新maxRange
class Solution:
  def canJump(self, nums):
    maxRange = 0
    for index, jump in enumerate(nums):
      if index > maxRange:
        return False
      maxRange = max(maxRange, index + jump)
    return True