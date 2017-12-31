# 380_Insert Delete GetRandom O(1)
# 一个list, 一个dict分别保存内容和坐标
# remove的时候, 交换list最后项和待删项, 然后修改dict中两个内容的坐标, 最后pop掉

import random

class RandomizedSet:
  def __init__(self):
    self.nums = []
    self.pos = {}

  def insert(self, val):
    if val in self.pos:
      return False
    self.nums.append(val)
    self.pos[val] = len(self.nums) - 1
    return True

  def remove(self, val):
    if val not in self.pos:
      return False
    index, last = self.pos[val], self.nums[-1]
    self.nums[index] = last
    self.pos[last] = index
    self.nums.pop()
    self.pos.pop(val)
    return True

  def getRandom(self):
    return self.nums[random.randint(0, len(self.nums) - 1)]

