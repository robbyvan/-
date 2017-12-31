# 287. Find the Duplicate Number.py
# 类似linkedlist圈, 双指针1步长2步长, 相遇处在圈内
# 然后从头开始同步长, 相遇处是圈开始的地方(也就是相同数字处)
class Solution:
  def findDuplicate(self, nums):
    if len(nums) > 1:
      slow, fast = nums[0], nums[nums[0]]
      while slow != fast:
        slow = nums[slow]
        fast = nums[nums[fast]]
      fast = 0
      while fast != slow:
        fast = nums[fast]
        slow = nums[slow]
      return slow
    return None