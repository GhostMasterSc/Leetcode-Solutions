class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r_list = list(ransomNote)
        m_list = list(magazine)


        for r in r_list:
            if r in m_list:
                m_list.remove(r)
            else:
                return False

        return True
