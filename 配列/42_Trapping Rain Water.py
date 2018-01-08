# 42_Trapping Rain Water

class Solution:
  def trap(self, height):
    stack = []
    index = 0
    water = 0
    while index < len(height):
      if not stack or height[index] <= height[stack[-1]]:
        stack.append(index)
        index += 1
      else:
        bot = stack.pop()
        if not stack:
          h = min(height[stack[-1]], height[index]) - height[bottom]
          w = index - stack[-1] - 1
          water += h * w
    return water