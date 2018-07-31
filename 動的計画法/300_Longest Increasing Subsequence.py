# 300_Longest Increasing Subsequence
# 1)dp. opt[i]代表含i时的最大子序列长度, 所以是max{i => [0, n - 1]} (max{k => [0, i)} (opt[k] + 1)}
# 2)O(nlgn) 每当遇到一个新的数, 利用二分搜索更新到合适的位置(因为后出现的数, 对于相同长度的序列, 具有覆盖的效果)

class Solution:
  def lengthOfLIS(self, nums):
    tails = [0] * len(nums)
    maxLen = 0
    for num in nums:
      low, high = 0, maxLen
      while low < high:
        mid = low + (high - low) // 2
        if tails[mid] < num:
          low = mid + 1
        else:
          high = mid
      tails[low] = num
      maxLen = max(maxLen, low + 1)
    return maxLen
    
# class Solution:
#   def lengthOfLIS(self, nums):
#     if not nums:
#       return 0
#     n, maxLen = len(nums), 1
#     opt = [1] * n
#     for i in range(1, n):
#       for k in range(i - 1):
#         if nums[i] > nums[k]:
#           opt[i] = max(opt[i], opt[k] + 1)
#       maxLen = max(opt[i], maxLen)
#     return maxLen
