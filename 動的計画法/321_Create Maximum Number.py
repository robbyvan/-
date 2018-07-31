# 321_Create Maximum Number
# 划分成两个子问题
# 1)在一个数组中选出k位, 保证相对顺序, 使得最大 => getMax
# 2)拼接两个数组使得最大 => merge
# 对于(1), 使用栈, 定义可跳过次数drop = len(nums) - k: 总可选数字数目 - 目标数字数目 = 可跳过次数
# 每当遇到了一个数字比栈顶大, 且还有可跳过次数, 就弹出栈顶(while直到递减或用尽跳过次数或栈空), 最后返回res[:k]即可
# 对于(2), 依次填入更大的首位即可

class Solution:
  def maxNumber(self, nums1, nums2, k):
    def getMax(nums, k):
      skip = len(nums) - k
      res = []
      for num in nums:
        while res and skip and res[-1] < num:
          res.pop()
          skip -= 1
        res.append(num)
      return res[:k]

    def merge(num1, num2):
      res = []
      while num1 or num2:
        if num1 > num2:
          res.append(num1.pop(0))
        else:
          res.append(num2.pop(0))
      return res

    l1, l2 = len(nums1), len(nums2)
    res = []
    for i in range(max(0, k - l2), min(k, l1) + 1):
      temp = merge(getMax(nums1, i), getMax(nums2, k - i))
      res = max(temp, res)
    return res

      