# 273_Integer to English Words
# xxx(billion), xxx(million), xxx(thousand), xxx
# 每段的xxx叫法相同, 因此使用helper处理每段, 最后补上B,M,TH
# 外层循环每次 %1000, 如果非零则叫, 否则不叫
# 内层三种情况: 1-19直接叫; 20<x<100 十位(/10) + helper(%10); x>100 百位(/100) + helper(%100)
# 注意情况之间的空格. 在<19后补" ", 递归时不用在末尾补" "了.

class Solution:
  def numberToWords(self, num):
    thousands = ["", "Thousand", "Million", "Billion"]
    if num == 0:
      return "Zero"
    res = ""
    for i in range(len(thousands)):
      if num % 1000 != 0:
        res = self.helper(num % 1000) + thousands[i] + " " + res
      num = num / 1000
    return res.strip()

  def helper(self, num):
    to19 = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
    tens = ["","Ten","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
    if num  == 0:
      return ""
    elif num < 20:
      return to19[num] + " "
    elif num < 100:
      return tens[num / 10] + " " + self.helper(num % 10)
    else:
      return to19[num / 100] + " Hundred" + self.helper(num % 100)
