# 88. Merge Sorted Array
# 逆序整合, 双指针, 如果2末 > 1末, p2补到最后否则p1补到最后
# 最后的指针: m + n - 1, p1: m - 1, p2: n - 1

class Solution:
  def merge(self, nums1, m, nums2, n):
    while n > 0:
      if m <= 0 or nums2[n - 1] >= nums1[m - 1]:
        nums1[m + n - 1] = nums2[n - 1]
        n -= 1
      else:
        nums1[m + n - 1] = nums1[m - 1]
        m -= 1