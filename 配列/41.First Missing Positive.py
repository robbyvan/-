# 41.First Missing Positive
# 寻找第一个missing的正数, 一定是1~N+1中间的一个
# 遍历两次, 第一次利用数组坐标对应存储存在的正数
# 此处要循环交换直到不能再交换为止(只交换属于1~N之间的正数) 并且这个数不能重复.(检查curr和nums[curr - 1]是不是相同)
# 第二次找到第一个不对应的坐标


class Solution:
  def firstMissingPositive(self, nums):
    if not nums:
      return 1

    for initIndex in range(len(nums)):
      curr = nums[initIndex]
      while curr > 0 and curr < len(nums) + 1 and curr != nums[curr - 1]:
        temp = nums[curr - 1]
        nums[curr - 1] = curr
        curr = temp

    for i in range(len(nums)):
      if (i + 1) != nums[i]:
        return i + 1

    return len(nums) + 1