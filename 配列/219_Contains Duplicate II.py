# 219. Contains Duplicate II
# 利用hash table, 检测HT里是否遇见过该元素, 如果有, 再检查坐标差.
# 每次遍历数字时添加进HT当中.
class Solution:
  def containsNearbyDuplicate(self, nums, k):
    d = {}
    for index, item in enumerate(nums):
      if item in d and index - d[item] <= k:
        return True
      d[item] = index
    return False