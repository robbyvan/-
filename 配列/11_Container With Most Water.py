# 11. Container With Most Water
# 从最宽开始, 双指针移动更新最大面积(贪心)
class Solution:
  def maxArea(self, height):
    if len(height) == 0:
      return 0
    maxWater = 0;
    left, right = 0, len(height) - 1
    while left < right:
      water = (right - left) * min(height[left], height[right])
      maxWater = max(maxWater, water)
      if height[left] < height[right]:
        left += 1
      else:
        right -= 1
    return maxWater
