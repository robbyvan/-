# 57_Insert Interval
# 先添加不相交的interval: 比较新的左右和旧的右左的大小
# 如果遇到新右比旧左大或者新左比旧右小, 则有相交
# 对于相交的两个区间, 更新新的相交, 取[min(), max()]
# 最后添加进去最终merge好的区间


class Solution:
  def insert(self, intervals, newInterval):
    res = []
    insertPos = 0
    for interval in intervals:
      if newInterval.start > interval.end:
        res.append(interval)
        insertPos += 1
      elif newInterval.end < interval.start:
        res.append(interval)
      else:
        newInterval.start = min(interval.start, newInterval.start)
        newInterval.end = max(interval.end, newInterval.end)
    res.insert(insertPos, newInterval)
    return res