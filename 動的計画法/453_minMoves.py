# 453_minMoves

class Solutin:
  def minMoves(self, nums):
    if not nums

# class Solution:
#   def minMoves(self, nums):
#     count = 0
#     minVal, maxVal = min(nums), max(nums)
#     while minVal < maxVal:
#       maxIndex = nums.index(maxVal)
#       for i in range(len(nums)):
#         if i != maxIndex:
#           nums[i] += (maxVal - minVal)
#       count += (maxVal - minVal)
#       minVal, maxVal = min(nums), max(nums)
#     return count

# class Solution:
#   def minMoves(self, nums):
#     if not nums:
#       return 0
#     return self.helper(nums, 0)
  
#   def helper(self, nums, count):
#     minVal, maxVal = min(nums), max(nums)
#     if minVal == maxVal:
#       return count
#     maxIndex = nums.index(maxVal)
#     for i in range(len(nums)):
#       if i != maxIndex:
#         nums[i] += 1
#     return self.helper(nums, count + 1)