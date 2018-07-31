# 112_Path Sum
# 递归
# 如果是none, false
# 如果没有孩子, 且val == target, true
# 否则return左或右的target - node.val

class Solution:
  def hasPathSum(self, root, target):
    if not root:
      return False
    if not root.left and not root.right and root.val == target:
      return True
    target = target - root.val
    return self.hasPathSum(root.left, target) or self.hasPathSum(root.right, target)

  # def hasPathSum(self, root, target):
  #   if not root:
  #     return False
  #   return self.helper(root, 0, target)

  # def helper(self, node, prevSum, target):
  #   if not node.left and not node.right:
  #     if prevSum + node.val == target:
  #       return True
  #   left, right = False, False
  #   if node.left:
  #     left = self.helper(node.left, prevSum + node.val, target)
  #   if node.right:
  #     right = self.helper(node.right, prevSum + node.val, target)
  #   return left or right