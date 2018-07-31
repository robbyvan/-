# 337_House Robber III
# 基本: self.helper(root.left.left, memo) + self.helper(root.left.right, memo) + self.helper(root.right.left, memo) + self.helper(root.right.right, memo) + root.val
# 和self.helper(root.left, memo) + self.helper(root.right, memo)比较, 取更大的值
# 但是有重复问题. 因为只保留了最佳的答案, 但是并不知道每个点的状态.
# 考虑用2个变量, 如果不取这个点, 如果取这个点, 分别的最大值.
# 问题只用考虑相邻两层了. 如果不抢这个点, 那么下层状态随便, 取max即可: notRobSum = max(left) + max(right)
# 如果抢这个点, 那么下层不能抢: robSum = left[0] + right[0] + root.val
# 在root处求max即可

class Solution:
  def rob(self, root):
    res = self.helper(root)
    return max(res)

  def helper(self, root):
    if not root:
      return [0, 0]
    left = self.helper(root.left)
    right = self.helper(root.right)
    notRobSum = max(left) + max(right)
    robSum = left[0] + right[0] + root.val
    return [notRobSum, robSum]

  # def rob(self, root):
  #   memo = collections.defaultDict(int)
  #   return self.helper(root, memo)

  # def helper(self, root, memo):
  #   if not root:
  #     return 0
  #   val = 0
  #   if root.left:
  #     val += self.helper(root.left.left, memo) + self.helper(root.left.right, memo)
  #   if root.right:
  #     val += self.helper(root.right.left, memo) + self.helper(root.right.right, memo)

  #   val = max(val + root.val, self.helper(root.left, memo) + self.helper(root.right, memo))
  #   memo[root] = val

  #   return val