# 383_Ransom Note
# hash表分别统计即可
class Solution:
  def canConstruct(self, ransomNote, magazine):
    return not collections.Counter(ransomNote) - collections.Counter(magazine)