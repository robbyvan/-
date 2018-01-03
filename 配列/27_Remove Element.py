# 27_Remove Element
# 同26, 交换条件 num != val

class Solution:
  def removeElement(self, nums, val):
    tail = 0
    for num in nums:
      if num != val:
        nums[tail] = num
        tail += 1
    return tail