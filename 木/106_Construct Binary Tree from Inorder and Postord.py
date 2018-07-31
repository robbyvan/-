# 106_Construct Binary Tree from Inorder and Postorder Traversal
# 同105

class Solution:
  def buildTree(self, inorder, postorder):
    if not inorder or not postorder:
      return None

    root = TreeNode(postorder.pop())
    rootIndex = inorder.index(root.val)

    root.left = self.buildTree(inorder[:rootIndex], postorder)
    root.right = self.buildTree(inorder[rootIndex+1:], postorder)

    return root