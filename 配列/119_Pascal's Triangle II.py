# 119_Pascal's Triangle II
# 同理path.append(last[i] + last[i - 1])
class Solution:
  def getRow(self, rowIndex):
    if rowIndex < 0:
      return []
    if rowIndex == 0:
      return [1]
    if rowIndex == 1:
      return [1, 1]
    last = [1]
    for row in range(2, rowIndex + 2):
      path = []
      for i in range(len(last)):
        if i == 0:
          path.append(1)
        else:
          path.append(last[i] + last[i - 1])
      path.append(1)
      last = path
    return last

