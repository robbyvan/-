# 217. Contains Duplicate
# 集合去重, 如果不在集合就add.
class Solution:
  def containsDuplicate(self, nums):
    s = set([])
    for num in nums:
      if num in s:
        return True
      s.add(num)
    return False
