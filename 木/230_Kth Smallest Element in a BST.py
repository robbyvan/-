# 230_Kth Smallest Element in a BST
# 前序遍历一次即可, 按k取出

class Solution:
  def kthSmallest(self, root, k):
    res = []
    if not root:
      return res
    self.helper(root, res)
    return res[k - 1]

  def helper(self, root, res):
    if not root:
      return
    self.helper(root.left, res)
    res.append(root.val)
    self.helper(root.right, res)
