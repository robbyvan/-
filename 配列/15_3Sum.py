# 15. 3 Sum
# 1. 排序, 外层循环数组, 注意跳过重复数字(同数字时, 后面的解必是前面数字解的子集)
# 2. 内层定义[左, 右], 求和与目标比较, 双指针移动
# 3. 相等时加入结果, 移动内层双指针(因为unique triplets, 都要移动1位)

# class Solution:
#   def threeSum(self, nums):
#     nums.sort()
#     length = len(nums)
#     for i in range(0, length - 2):
#       if i > 0 and nums[i] == nums[i - 1]:
#         continue
#       left, right = i + 1, length - 1
#       while left < right: 
#         s = nums[i] + nums[left] + nums[right]
#         if s < 0:
#           left += 1
#         elif s > 0:
#           right -= 1
#         else:
#           res.append([nums[i], nums[left], nums[right]])
#           while left < right and nums[left] == nums[left + 1]:
#             left += 1
#           while left < right and nums[right] == nums[right - 1]:
#             right -= 1
#           left += 1
#           right -= 1
#       return res