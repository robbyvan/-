# 120_Triangle
# dp. 只用记录上一层的dp结果
# 递推公式: dp2.append(min(dp[j - 1], dp[j]) + row[j])
# 下层的j由上层j - 1和j决定
class Solution:
  def minimumTotal(self, triangle):
    if not triangle:
      return 0
    if len(triangle) == 1:
      return triangle[0][0]
    dp = [triangle[0][0]]
    for i in range(1, len(triangle)):
      row = triangle[i]
      dp2 = []
      for j in range(len(row) - 1):
        if j == 0:
          dp2.append(dp[0] + row[0])
        else:
          dp2.append(min(dp[j - 1], dp[j]) + row[j])
      dp2.append(dp[-1] + row[-1])
      dp = dp2
    return min(dp)