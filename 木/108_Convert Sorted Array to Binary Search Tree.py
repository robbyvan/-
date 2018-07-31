# 108_Convert Sorted Array to Binary Search Tree
# 树是递归定义. 从中间递归生成即可.

class Solution:
  def sortedArrayToBST(self, nums):
    if not nums:
      return None

    mid = len(nums) // 2

    root = TreeNode(nums[mid])
    root.left = self.sortedArrayToBST(nums[:mid])
    root.right = self.sortedArrayToBST(nums[mid + 1:])

    return root