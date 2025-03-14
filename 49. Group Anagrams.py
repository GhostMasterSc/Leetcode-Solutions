from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dict_anag = defaultdict(list)

        for words in strs:
            counter = [0]*26
            for s in list(words):
                position = ord(s)-ord('a')
                counter[position]+=1

            dict_anag[tuple(counter)].append(words)


        return list(dict_anag.values())
        
            
            
           

