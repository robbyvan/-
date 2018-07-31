# 116_Populating Next Right Pointers in Each Node
# 按照定义逐层修改. 双重循环 (层间nextLevelStart = root.left, 层内root = root.next + )
# 如果不是最后一行, root.left.next = root.right, root.right.next = None if root.next is None else root.next.left

class Solution:
  def connect(self, root):
    if not root:
      return None
    while root and root.left:
      nextLevelStart = root.left
      while root:
        root.left.next = root.right
        root.right.next = None if root.next is None else root.next.left
        root = root.next
      root = nextLevelStart
