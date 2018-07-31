# 174_Dungeon Game
# 要求王子血量随时满足hp + dungeon[i, j] >= 1 => hp >= 1 - dungeon[i, j] => 取最小, hp = 1 - dungeon[i, j]
# 要求最小hp, 如果到最后一个格子, 尽可能是1点血, 所以是1 - d[i, j]
# 对于格子[i, j], 需要满足hp = 下一处要求的血量 - d[i, j]. 
# (因为求最小的血量, 所以下一个格子血量也是尽可能的少的走法) 
# => hp[i][j] = max(1, min(hp[i + 1][j], hp[i][j + 1])) - dungeon[i][j]

class Solution:
  def calculateMinimumHP(self, dungeon):
    m, n = len(dungeon), len(dungeon[0])
    hp = [[1] * n for _ in range(m)]
    for i in range(m - 1, -1, -1):
      for j in range(n - 1, -1, -1):
        if i == m - 1 and j == n - 1:
          hp[i][j] = max(1, 1 - dungeon[i][j])
        elif i == m - 1:
          hp[i][j] = max(1, hp[i][j + 1] - dungeon[i][j])
        elif j == n + 1:
          hp[i][j] = max(1, hp[i][j + 1] - dungeon[i][j])
        else:
          hp[i][j] = max(1, min(hp[i][j + 1], hp[i + 1][j]) - dungeon[i][j])
    return hp[0][0]

