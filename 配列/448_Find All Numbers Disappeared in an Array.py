# 448. Find All Numbers Disappeared in an Array
# 内容还是1~n, 有两次重复的数字.
# 类似, 每次翻转对应index处内容的正负值, 如果遇到了已经的负值的内容, 就不再翻转此index的内容了.
# 那么第二次遍历的时候, 因为有内容缺省, 那么缺省index处的内容一定是正的, 因为没有翻转过
# 所以只要按index找到nums[index]是正的位置就好了.
class Solution:
  def findDisappearedNumbers(self, nums):
    res = []
    for num in nums:
      if nums[abs(num) - 1] < 0:
        continue
      nums[abs(num) - 1] *= -1

    for i in range(len(nums)):
      if nums[i] > 0:
        res.append(i + 1)

    return res