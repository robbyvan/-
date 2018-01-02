# 56. Merge Intervals
# 先对intervals排序, 按照区间起点.
# 遍历一次, 如果item.start比现在末小, 更新右为二者max
# 否则直接添加.

class Solution:
  def merge(self, intervals):
    if not intervals:
      return []
    intervals = sorted(intervals, key = lambda x: x.start)
    res = [intervals[0]]
    for item in intervals:
      if item.start <= res[-1].end:
        res[-1].end = max(res[-1].end, item.end)
      else:
        res.append(item)
    return res