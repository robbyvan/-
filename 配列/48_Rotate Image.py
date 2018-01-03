# 48_Rotate Image
# 顺时针旋转: 上下颠倒, 对称对角线
# 逆时针旋转: 左右颠倒, 对称对角线

class Solution:
  def rotate(self, matrix):
    matrix = self.swap(matrix, 0, len(matrix) - 1)
    for i in range(len(matrix)):
      for j in range(0, i):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


  def swap(self, nums, l, r):
    while l < r:
      nums[l], nums[r] = nums[r], nums[l]
      l += 1
      r -= 1
    return nums
