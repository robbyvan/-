# 128. Longest Consecutive Sequence
# 建立hash表, 每个连续段都保存长度(主要是边界)
# 当遇到一个新数字, 检查他的左右, 相加就是长度
class Solution:
  def longestConsecutive(self, nums):
    if not nums:
      return 0
    res, d = 1, {}
    for num in nums:
      if num not in d:
        left = d.get(num - 1, 0)
        right = d.get(num + 1, 0)
        length = left + right + 1
        d[num] = length
        res = max(length, res)
        d[num - left] = length
        d[num + right] = length
    return res
