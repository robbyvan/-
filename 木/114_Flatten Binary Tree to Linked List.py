# 114_Flatten Binary Tree to Linked List
# 递归. 如果node.left, node.right已经flatten了. 
# 那么对于node, 只用把处理好的right拼在left后面

class Solution:
  def flatten(self, root):
    if not root:
      return
    left, right = root.left, root.right
    self.flatten(left)
    self.flatten(right)
    root.left, root.right = None, left
    p = root
    while p.right:
      p = p.right
    p.right = right
