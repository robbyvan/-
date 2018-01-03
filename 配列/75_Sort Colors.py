# 75_Sort Colors
# 分成三堆, 利用三个指针low记录空的0, high记录空的2, mid和high共同完成数组扫描
# 如果遇到了0, 交换low mid并都前进1
# 如果遇到了1, 前进mid, 留在中间
# 如果遇到了2, 交换mid high, 前进high, mid保持不动
# mid > high时扫描结束

class Solution:
  def sortColors(self, nums):
    temp, low, mid, high = 0, 0, 0, len(nums) - 1
    while mid <= high:
      if nums[mid] == 0:
        nums[low], nums[mid] = nums[mid], nums[low]
        mid += 1
        low += 1
      elif nums[mid] == 1:
        mid += 1
      elif nums[mid] == 2:
        nums[mid], nums[high] = nums[high], nums[mid]
        high -= 1
