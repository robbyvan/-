# 105_Construct Binary Tree from Preorder and Inorder Traversal
# 前后序找根, 中序分左右, 递归生成左右子树.

class Solution:
  """
  TreeNode(val)
  """
  def buildTree(self, preorder, inorder):
    if not preorder or not inorder:
      return None

    root = TreeNode(preorder.pop(0))
    rootIndex = inorder.index(root.val)

    root.left = self.buildTree(preorder, inorder[:rootIndex])
    root.right = self.buildTree(preorder, inorder[rootIndex + 1:])

    return root

