# 84. Largest Rectangle in Histogram
# 考虑递增, 开始递减时, 计算递减前每个bar到递减处的面积: height[stack[-1]] * width
# 其中width = i - stack[-1] - 1 或者全部i - 0
# 一开始height补0, 为了最后计算一次全部

class Solution:
  def largestRectangleArea(self, height):
    height.append(0)
    stack = [0]
    area = 0
    for i in range(1, len(height)):
      while stack and height[i] < height[stack[-1]]:
        h = height[stack.pop()]
        w = i if not stack else i - stack[-1] - 1
        area = max(area, w * h)
      stack.append(i)
    return area

# class Solution:
#   def largestRectangleArea(self, height):
#     return self.helper(height)
#   def helper(self, heights):
#     if len(heights) == 0:
#       return 0
#     minHeight = min(heights)
#     minIndex = heights.index(minHeight)
#     leftMax = self.helper(heights[:minIndex])
#     rightMax = self.helper(heights[minIndex+1:])
#     flatArea = minHeight * len(heights)
#     return max(leftMax, rightMax, flatArea)