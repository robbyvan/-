# 169. Majority Element
# 还可以排序找中间, hash表
# 投票: 相同cand => ++;不同cand => --;减到0时 重置成1票 修改cand

class Solution:
  def majorityElement(self, nums):
    count, cand = 0, 0
    for num in nums:
      if num == cand:
        count += 1
      elif count == 0:
        cand, count = num, 1
      else:
        count -= 1
    return cand