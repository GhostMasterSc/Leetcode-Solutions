class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first_word = strs[0]
        scan = len(first_word)
        count = scan
        for i in range(1,len(strs)):
            count = 0
            if scan>len(list(strs[i])):
                scan = len(list(strs[i]))

            for j in range(scan):
                if list(first_word)[j]!=list(strs[i])[j]:
                    break
                count+=1
            if count<scan:
                scan=count
                
            if scan==0:
                break

        print(count)
        
        if count==0 :
            return ""
        else:
            return first_word[:count]
