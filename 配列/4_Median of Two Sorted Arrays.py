# 4. Median of Two Sorted Arrays
# 二分法
# 首先判断奇偶, 奇数就找l // 2, 偶数就是中间两个 (l // 2) 和 (l // 2 - 1) 的平均值
# 递归寻找kth, 找到ia, ib(两个数组的中间坐标)和对应的值ma, mb, 比较k和ia + ib的大小
# 如果k更大, 说明ab二者中前ia或ib个数字一定没有要找的k, (k一定比按顺序拼起来的前ia或ib个都更大)
# 因此比较ma和mb, 小的数组的前ia或ib个可以扔掉(a[ia + 1:]), 并更新k为k - ia(或ib) - 1
# 同理k更小的时候, 扔掉a或b的后ia或ib部分(a[:ia]), 但不用更新k, 因为是找小.
# 注意边界和小数除法.

class Solution:
  def findMedianSortedArrays(self, A, B):
    l = len(A) + len(B)
    if l % 2 == 1:
      return self.kth(A, B, l // 2)
    else:
      return (self.kth(A, B, l // 2) + self.kth(A, B, l // 2 - 1)) / 2.0

  def kth(self, A, B, k):
    if not A:
      return B[k]
    if not B:
      return A[k]
    ia, ib = len(A) // 2, len(B) // 2
    ma, mb = A[ia], B[ib]
    if ia + ib < k:
      if ma > mb:
        return self.kth(A, B[ib + 1:], k - ib - 1 )
      else:
        return self.kth(A[ia + 1:], B, k - ia - 1 )
    else:
      if ma > mb:
        return self.kth(A[:ia], B, k)
      else:
        return self.kth(A, B[:ib], k)