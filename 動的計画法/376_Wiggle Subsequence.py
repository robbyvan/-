# 376_Wiggle Subsequence
# 每个数字有两个状态 => 到这里是+, 到这里是-
# 如果nums[i] > nums[i - 1], 是 + , 更新up[i] = down[i - 1] + 1, down保持
# 证明, 假设i - 1的但是最后一位是N, 如果nums[i] > i, 显然; 如果nums[i] < N, 而在N处是N比之前小, 那么可以把N换成nums[i - 1], nums[i - 1]也一定保持了递减.
# 如果nums[i] < nums[i - 1], 是 -, 更新down[i] = up[i - 1] + 1, up保持
# 相等, 都保持

class Solution:
  def wiggleMaxLength(self, nums):
    if len(nums) == 0:
      return 0
    up = [1] * len(nums)
    down = [1] * len(nums)
    
    for i in range(1, len(nums)):
      if nums[i] > nums[i - 1]:
        up[i] = down[i - 1] + 1
        down[i] = down[i - 1]
      elif nums[i] < nums[i - 1]:
        up[i] = up[i - 1]
        down[i] = up[i - 1] + 1
      else:
        up[i] = up[i - 1]
        down[i] = down[i - 1]

    return max(up[-1], down[-1])

