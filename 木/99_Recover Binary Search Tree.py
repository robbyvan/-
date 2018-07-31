# 99_Recover Binary Search Tree

class Solution:
  def __init__(self):
    self.first = None
    self.second = None
    self.prev = TreeNode(float("-inf"))

  def recoverTree(self, root):
    self.inorder(root)
    self.first.val, self.second.val = self.second.val, self.first.val

  def inorder(self, root):
    if not root:
      return
    self.inorder(self.left)
    if not first and root.val <= prev.val:
      self.first = self.prev
    if first and root.val <= prev.val:
      self.second = root
    prev = root
    self.inorder(self.right)