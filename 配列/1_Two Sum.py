# 1_Two Sum
# 哈希表
# 把target - nums[i]存入(存入差的那一部分)
# 每次遇到新num, 检查是否是d中差的数字, 如果有, 说明有解, 返回即可

class Solution:
  def twoSum(self, nums, target):
    if len(nums) <= 1:
      return False
    d = {}
    for i in range(len(nums)):
      if nums[i] in d:
        return [d[nums[i]], i]
      else:
        d[target - nums[i]] = i