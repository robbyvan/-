# 100_Same Tree
# 如果都None => True
# 如果一个None => False
# 如果值不同 => False
# 如果值相同 => 看左右子树

class Solution:
  def isSameTree(self, p, q):
    if not p and not q:
      return True
    if not p or not q:
      return False
    if p.val != q.val:
      return False
    return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)