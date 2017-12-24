# 442_Find All Duplicates in an Array
# 1 ≤ a[i] ≤ n (n = size of array)
# 每个内容都在1~n, 那么内容作为index, 每次翻转index处内容的正负, 然后如果遇到了第二次, 准备翻转时一定是负内容, 则添加到res中.
class Solution:
  def findDuplicates(self, nums):
    res = []
    for num in nums:
      if nums[abs(num) - 1] < 0:
        res.append(abs(num))
      else:
        nums[abs(num) - 1] *= -1
    return res