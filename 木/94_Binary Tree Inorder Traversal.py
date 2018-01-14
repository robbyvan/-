# 94_Binary Tree Inorder Traversal
# 递归算法: 中序遍历 = 左中右
# 非递归算法: 从根出发, 向左移动, 经过节点进栈, 直到null后pop访问栈顶node, 修改下一个节点为node.

class Solution:
  def inorderTraversal(self, root):
    res = []
    self.helper(root, res)
    return res

  def helper(self, root, res):
    if root is None:
      return
    self.helper(root.left)
    res.append(root.val)
    self.helper(root.right)

  def inorderTraversal(self, root):
    stack, res = [], []
    while True:
      while root:
        stack.append(root)
        root = root.left
      if stack:
        node = stack.pop()
        res.append(node.val)
        root = node.right
      else:
        return res

    





