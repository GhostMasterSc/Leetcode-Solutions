class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        list_s = list(str(s))
        list_t = list(str(t))
        
        answer=False
        index = 0


        if len(list_s)==0:
            answer=True
        else:
            for l in list_t:
                if l==list_s[index]:
                    index+=1
                if index==len(list_s):
                    answer=True
                    break
    
        return answer
       
        
