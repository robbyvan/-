# 189_Rotate Array
# 注意k比n大的情况, 求余.
# 然后两部分拼起来就好了
class Solution(object):
  def rotate(self, nums, k):
    n = len(nums)
    k = k % n
    index = n - k
    nums[:] = nums[index:] + nums[:index]