# 105. Construct Binary Tree from Preorder and Inorder Traversal
# 后序: 左右根
# 中序: 左根右
# 前序: 根左右
# 
# 前后序找根, 中序划分出左 右子树. 因为树是递归结构, 把左右子树的中序持续划分, 新的前后序找根.(需要pop掉之前的根.) 

class Solution:
  def buildTree(self, preorder, inorder):
    if not preorder or not inorder:
      return None

    root = TreeNode(preorder.pop(0))
    rootIndex = inorder.index(root.val)

    root.left = self.buildTree(preorder, inorder[:rootIndex])
    root.right = self.buildTree(preorder, inorder[rootIndex+1:])

    return root