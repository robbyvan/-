# 85.Maximal Rectangle
# 类似hist最大面积, 把二维按row遍历计算.

class Solution:
  def maxArea(self, heights):
    stack = [0]
    area = 0
    for i in range(1, len(heights)):
      while stack and heights[i] < heights[stack[-1]]:
        h = heights[stack.pop()]
        w = i if not stack else i - stack[-1] - 1
        area = max(area, h * w)
      stack.append(i)
    return area

  def maximalRectangle(self, matrix):
    if not matrix or not matrix[0]:
      return 0
    m, n = len(matrix), len(matrix[0])
    heights = [0] * (n + 1)
    res = 0
    for row in matrix:
      for j in range(n):
        heights[j] = heights[j] + 1 if row[j] == '1' else 0
      res = max(res, self.maxArea(heights))
    return res