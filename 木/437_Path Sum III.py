# 437_Path Sum III
# 构造helper(node, target, targets)
# 其中targets = [t - node.val for t in targets]
# 如果None, 返回0次. 否则检查该点能否组成一条路(在目标dict中), 创造下一个点(node.left/right)新targets.(t - node.val)

class Solution:
  def pathSum(self, root, target):
    if not root:
      return 0
    return self.helper(root, target, [target])

  def helper(self, node, target, targets):
    if not node:
      return 0
    hit = 0
    for t in targets:
      if t == node.val:
        hit += 1
    targets = [t - node.val for t in targets] + [target]
    return hit + self.helper(node.left, target, targets) + self.helper(node.right, target, targets)
