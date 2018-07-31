# 450_Delete Node in a BST
# 递归删除(先找), 如果更小, 递归操作左子树, 更大则右子树
# 找到后. 如果左子树空, 返回右子树; 右子树空, 返回左子树
# 左右都有, 找左子树最大或者右子树最小, 修改父节点的值, 最后删掉替换的节点(调用自己)

class Solution:
  def deleteNode(self, root, key):
    if not root:
      return None
    if key < root.val:
      root.left = self.deleteNode(root.left, key)
    elif key > root.val:
      root.right = self.deleteNode(root.right, key)
    else:
      if not root.left:
        return root.right
      elif not root.right:
        return root.left
      else:
        leftMax = self.findMax(root.left)
        root.val = leftMax.val
        root.left = self.deleteNode(root.left, leftMax.val)
    return root

  def findMax(self, node):
    while node.right:
      node = node.right
    return node