from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = Counter(s)
        dict_t = Counter(t)

        if dict_t == dict_s:
            return True
        else:
            return False
