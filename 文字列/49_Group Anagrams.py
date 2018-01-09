# 49_Group Anagrams
# 排序各项, 利用hash表, 保存变形前的单词.

class Solution:
  def groupAnagrams(self, strs):
    d = {}
    for w in sorted(strs):
      key = tuple(sorted(w))
      d[key] = d.get(key, []) + [w]
    return d.values()

# import collections
# class Solution:
#   def groupAnagrams(self, strs):
#     res = []
#     d = collections.defaultdict(set)
#     for i, item in enumerate(strs):
#       standard = tuple(sorted(item))
#       d[standard].add(i)
#     for key in d:
#       path = []
#       for index in d[key]:
#         path.append(strs[index])
#       res.append(path)
#     return res

# a = Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
# print(a)


        
    
    