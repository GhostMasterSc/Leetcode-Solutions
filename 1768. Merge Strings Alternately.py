class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        new = ""
        index_1 = 0 
        word1 = list(word1)
        word2 = list(word2)
        index_2 = 0
        switch = 1
        for i in range(len(word1)+len(word2)):
            if switch==1:
                new = new + word1[index_1]
                index_1 +=1
                if index_2<len(word2):
                    switch=0
            else:
                new = new + word2[index_2]
                index_2 +=1
                if index_1<len(word1):
                    switch=1
            print(new)

        return new
