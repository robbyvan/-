# 414_Third Maximum Number
# 一个队列, 保存前三大, 循环一次更新三个变量就好.

class Solution:
  def thirdMax(self, nums):
    queue = [float('-inf'), float('-inf'), float('-inf')]
    for num in nums:
      if num not in queue:
        if num > queue[0]: 
          queue = [num, queue[0], queue[1]]
        elif num > queue[1]:
          queue = [queue[0], num, queue[1]]
        elif num > queue[2]:
          queue = [queue[0], queue[1], num]
    return queue[2] if queue[2] != float('-inf') else max(queue)