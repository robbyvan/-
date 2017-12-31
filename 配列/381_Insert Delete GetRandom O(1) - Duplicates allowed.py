# 381. Insert Delete GetRandom O(1) - Duplicates allowed
# 只是一个内容有了多个对应的坐标, 因此dict右边改成一个set
# 删除的时候, 先找到pos[val], 取出set最后一个坐标, 然后交换nums的待删内容和最后一个内容
# 然后向最后一个内容对应的dict的set里面加上刚刚的坐标, 再删除原来的-1坐标值
# 最后pop掉nums最后一项.

import random
class RandomizedCollection:
  def __init__(self):
    self.nums = []
    self.pos = collections.defaultdict(set)

  def insert(self, val):
    self.nums.append(val)
    self.pos[val].add(len(self.nums) - 1)
    return True

  def remove(self, val):
    if not self.pos[val]:
      return False
    index = self.pos[val].pop()
    last = self.nums[-1]
    self.nums[index] = last
    self.pos[last].add(index)
    self.pos[last].remove(len(self.nums) - 1)
    self.nums.pop()
    return True

  def getRandom(self):
    return random.choice(self.nums)
    
