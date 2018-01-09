# 12_Integer to Roman
# 按照位定义拼: 千 + 百 + 十 + 个

class Solution:
  def intToRoman(self, num):
    roman = { 1: 'I', 10: 'X', 100: 'C', 1000: 'M', 5: 'V', 50: 'L', 500: 'D' }
    M = ["", "M", "MM", "MMM"]
    C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    return M[num / 1000] + C[num % 1000 / 100] + X[num % 100 / 10] + I[num % 10]