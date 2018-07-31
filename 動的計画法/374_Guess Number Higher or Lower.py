# 374_Guess Number Higher or Lower
# 二分搜索

class Solution:
  def guessNumber(self, n):
    low, high = 1, n
    while low < high:
      mid = low + (high - low) / 2
      check = guess(mid)
      if  check < 0:
        high = mid
      elif check > 0:
        low = mid + 1
      else:
        return mid
    return low