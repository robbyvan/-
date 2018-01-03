# 74_Search a 2D Matrix
# 看成一个m * n的有序数字
# 行n / col, 列n % col

class Solution(object):
  def searchMatrix(self, matrix, target):
    if not matrix or not matrix[0]:
      return False
    m, n = len(matrix), len(matrix[0])
    low, high = 0, m * n - 1
    while low < high:
      mid = low + (high - low) / 2
      num = matrix[mid / n][mid % n]
      if num == target:
        return True
      elif num < target:
        low = mid + 1
      else:
        high = mid
    return True if matrix[low / n][low % n] == target else False
