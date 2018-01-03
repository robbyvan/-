# 495_Teemo Attacking
# 按定义就好
# 比较当前时间 + 时长 是否超过了下个时间点, 没有: +duration, 超过了: +时间差

class Solution:
  def findPoisonedDuration(self, timeSeries, duration):
    if not timeSeries or not duration:
      return 0
    # start = timeSeries[0]
    if len(timeSeries) == 1:
      return duration
    total = 0
    for i in range(len(timeSeries) - 1):
      start = timeSeries[i]
      end = start + duration - 1
      if end < timeSeries[i + 1]:
        total += duration
      else:
        total = total + (timeSeries[i + 1] - timeSeries[i])
    return total + duration