class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict_letter = {
            "M" : 1000,
            "D" : 500,
            "C" : 100,
            "L" : 50,
            "X" : 10,
            "V" : 5,
            "I" : 1
        }
        
        
        letter_list = list(s)
        value = 0

        for index in range(len(letter_list)-1):
            if dict_letter[letter_list[index]]< dict_letter[letter_list[index+1]]:
                current_value = - dict_letter[letter_list[index]]
            else:
                current_value =  dict_letter[letter_list[index]]
            value = value + current_value
            prev_letter = letter_list[index]


        value = value + dict_letter[letter_list[len(letter_list)-1]]

        return value
            

           

