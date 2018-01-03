# 228_Summary Ranges
# 按定义遍历
# 如果增量大于1说明断开了.
# 添加进这段, 注意最后while结束循环需要手动一次最后一段

class Solution:
  def summaryRanges(self, nums):
    if not nums:
      return []
    res, i , start = [], 0, 0
    while i < len(nums) - 1:
      if nums[i] + 1 != nums[i + 1]:
        res.append(self.printRange(nums[start], nums[i]))
        start = i + 1
      i += 1
    res.append(self.printRange(nums[start], nums[i]))
    return res

  def printRange(self, l , r):
    if l == r:
      return str(l)
    else:
      return str(l) + "->" + str(r)

    