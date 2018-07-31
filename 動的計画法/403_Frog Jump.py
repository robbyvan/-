# 403_Frog Jump
# 寻找路径问题: 利用dfs + memoization
# 对于尝试过错误的(起点, 基本步长), 直接返回False
# 如果起点 == 终点, true
# 如果步长0, 起点不在石头列表, false
# 否则尝试三种跳法的or, 如果true返回, 否则添加到memo里面记住错误的跳法

class Solution:
  def canCross(self, stones):
    self.memo = set()
    final = stones[-1]
    stones = set(stones)
    return self.jump(stones, 1, 1, final)
    
  def jump(self, stones, start, baseStep, final):
    if (start, baseStep) in self.memo:
      return False
    if start == final:
      return True
    if start not in stones or baseStep == 0:
      return False
    res = self.jump(stones, start + baseStep - 1, baseStep - 1, final) or self.jump(stones, start + baseStep, baseStep, final) or self.jump(stones, start + baseStep + 1, baseStep + 1, final)
    if res:
        return True
    self.memo.add((start, baseStep))
    return False