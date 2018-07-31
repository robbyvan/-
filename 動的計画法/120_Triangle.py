# 120_Triangle
# 见数组120

class Solution:
  def minimumTotal(self, triangle):
    if not triangle:
      return 0
    if len(triangle) == 1:
      return triangle[0][0]
    # n = len(triangle[-1])
    prev = [triangle[0][0]]

    for rowIndex in triangle(1, len(triangle)):
      curr = [prev[0] + triangle[rowIndex][0]]
      for j in range(1, len(prev)):
        curr += [min(prev[j - 1], prev[j]) + triangle[rowIndex][j]]
      curr += [prev[-1] + triangle[rowIndex][-1]]
      prev = curr
    return min(prev)


