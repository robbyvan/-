# 167_Two Sum II - Input array is sorted
# 和1类似, 每次遇到, 存入d{}
# 遇到新数, 检查他的互补数是否在d中, 如果有, 返回即可

class Solution:
  def twoSum(self, numbers, target):
    d = {}
    for i, num in enumerate(numbers):
      if target - num in d:
        return [d[target - num], i + 1]
      d[num] = i + 1