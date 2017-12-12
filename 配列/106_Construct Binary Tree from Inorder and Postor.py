# 106. Construct Binary Tree from Inorder and Postorder Traversal
# 后序: 左右根
# 中序: 左根右
# 前序: 根左右
# 
# 前后序找根, 中序划分出左 右子树. 因为树是递归结构, 把左右子树的中序持续划分, 新的前后序找根.(需要pop掉之前的根.) 
class Solution:
  def buildTree(self, inorder, postorder):
    if not inorder or not postorder:
      return None

    root = TreeNode(postorder.pop())
    rootIndex = inorder.index(root.val)

    root.right = self.buildTree(inorder[rootIndex+1:], postorder)
    root.left = self.buildTree(inorder[:rootIndex], postorder)

    return root