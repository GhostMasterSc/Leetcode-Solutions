from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        
        dict_text = defaultdict(int)
        for t in list(text):
            dict_text[t]+=1

        min_f = 100000
        for l in "balloon":
            if l=="l" or l=="o":
                if dict_text[l]//2 < min_f:
                    min_f = dict_text[l]//2
            else:
                if dict_text[l]<min_f:
                    min_f = dict_text[l]

        return min_f
