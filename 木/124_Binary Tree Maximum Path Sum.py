# 124_Binary Tree Maximum Path Sum
# 遍历规则: 求该节点为最高的父结点时, 所有路径的最大.
# 最大的路径: {左下 + 自己 + 右下} 或者 {自己 + max(左下 + 右下)} + {其他}
# 注意left, right要和0取max(), 因为如果本来是负数就更小了, 而0代表不要. 有一个下限

class Solution:
  def __init__(self):
    self.maxSeen = float("-inf")

  def maxPathSum(self, root):
    self.maxSumIfNodeIsHighestEnd(root)
    return self.maxSeen

  def maxSumIfNodeIsHighestEnd(self, node):
    if node is None:
      return 0
    optLeft = max(0, self.maxSumIfNodeIsHighestEnd(node.left))
    optRight = max(0, self.maxSumIfNodeIsHighestEnd(node.right))
    self.maxSeen = max(self.maxSeen, optLeft + optRight + node.val)
    return max(optLeft, optRight) + node.val
