# 101_Symmetric Tree
# 检查左右镜像:
# 都不存在 => true
# 存在不对称 => false
# 都存在:
# 根相同 => 左左 == 右右 and 左右 == 右左
# 根不同 => false

class Solution:
  def isSymmetric(self, root):
    if not root:
      return True
    return self.isMirror(root.left, root.right)

  def isMirror(self, left, right):
    if not left and not right:
      return True
    if not left or not right:
      return False
    if left.val == right.val:
      return self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)
    return False